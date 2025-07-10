import os
import requests

WHATSAPP_TOKEN = os.getenv("WHATSAPP_ACCESS_TOKEN",)
WHATSAPP_API_VERSION = os.getenv("WHATSAPP_API_VERSION")
PHONE_ID = os.getenv("WHATSAPP_PHONE_NUMBER_ID")

def get_whatsapp_media_url(media_id):
    url = f"https://graph.facebook.com/v19.0/{media_id}"
    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("url")
    raise Exception(f"Failed to get media URL: {response.text}")

def download_whatsapp_media(media_url):
    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}"
    }
    response = requests.get(media_url, headers=headers)
    if response.status_code == 200:
        return ("file", ("document", response.content))  # ready to use in files param
    raise Exception(f"Failed to download media: {response.text}")

def send_whatsapp_message(recipient_number, message):
    url = f"https://graph.facebook.com/{WHATSAPP_API_VERSION}/{PHONE_ID}/messages"
    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": recipient_number,
        "type": "text",
        "text": {"body": message}
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

def send_interactive_buttons(recipient_number, body_text, buttons):
    url = f"https://graph.facebook.com/{WHATSAPP_API_VERSION}/{PHONE_ID}/messages"
    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": recipient_number,
        "type": "interactive",
        "interactive": {
            "type": "button",
            "body": {"text": body_text},
            "action": {"buttons": buttons}
        }
    }

    response = requests.post(url, headers=headers, json=payload)
    return response.json()
