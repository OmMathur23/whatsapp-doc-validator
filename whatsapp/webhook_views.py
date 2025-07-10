import os
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt
from .utils import send_whatsapp_message, send_interactive_buttons, get_whatsapp_media_url, download_whatsapp_media
import json
user_state = {}

@csrf_exempt
@require_POST
def whatsapp_webhook(request):
    data = json.loads(request.body.decode("utf-8"))

    try:
        entry = data["entry"][0]["changes"][0]["value"]
        message = entry.get("messages", [])[0]
        sender_id = message.get("from")
    except Exception as e:
        print("[Webhook parsing error]", e)
        return JsonResponse({"error": "Invalid format"}, status=400)
    except Exception as e:
        return JsonResponse({"error": "Invalid format"}, status=400)

    if message.get("type") == "text":
        text = message["text"]["body"].strip().lower()

        if text in ["hi", "start", "verify", "doc", "document"]:
            send_interactive_buttons(
                to=sender_id,
                body_text="Which document do you want to verify?",
                buttons=[
                    {"type": "reply", "reply": {"id": "choose_pan", "title": "PAN"}},
                    {"type": "reply", "reply": {"id": "choose_aadhar", "title": "Aadhaar"}}
                ]
            )
            return JsonResponse({"status": "buttons sent"})

    if message.get("type") == "button":
        button_id = message["button"]["payload"]

        if button_id == "choose_pan":
            user_state[sender_id] = {"doc_type": "pan"}
            send_whatsapp_message(sender_id, "Please upload the PAN document.")
        elif button_id == "choose_aadhar":
            user_state[sender_id] = {"doc_type": "aadhar"}
            send_whatsapp_message(sender_id, "Please upload the Aadhaar document.")
        return JsonResponse({"status": "awaiting document"})


    if message.get("type") == "document" or message.get("type") == "image":
        doc_type = user_state.get(sender_id, {}).get("doc_type")
        if not doc_type:
            send_whatsapp_message(sender_id, "Please choose a document type first.")
            return JsonResponse({"status": "missing document type"})

        # Download the file
        media_id = message[message["type"]]["id"]
        try:
            media_url = get_whatsapp_media_url(media_id)
            file_tuple = download_whatsapp_media(media_url)

            # Forward to backend API
            endpoint = f"http://localhost:5000/api/validate/{doc_type}"
            res = requests.post(endpoint, files={file_tuple[0]: file_tuple[1]})
            result = res.json()

            if result.get("success") and result.get("data"):
                number = list(result["data"].values())[0]  # PAN or Aadhar number
                send_whatsapp_message(sender_id, f"✅ Verified: {number}")
            else:
                send_whatsapp_message(sender_id, "❌ Invalid document.")
        except Exception as e:
            send_whatsapp_message(sender_id, "⚠️ Failed to process your document.")
            print("[error]", e)
        return JsonResponse({"status": "document processed"})

    return JsonResponse({"status": "ignored"})
