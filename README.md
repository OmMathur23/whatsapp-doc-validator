WhatsApp Document Validator 🧾📲

A full-stack WhatsApp-based document verification system built using Django, Flask, and PaddleOCR.

Users can send a document (PAN or Aadhaar) via WhatsApp and receive real-time validation responses — all powered by backend OCR processing.

📸 Demo Video: (Add your YouTube/GIF/demo link here)

🚀 Live Deployment: (Add your Render/URL if deployed)

📂 Project Structure

whatsapp-doc-validator/
├── backend/ ← Flask OCR API for PAN & Aadhaar validation
│ ├── app.py ← API endpoints (/api/validate/pan, /aadhar)
│ ├── validators/ ← PAN and Aadhaar validation logic
│ ├── ocr_utils.py ← OCR & image preprocessing utilities
│ └── models/ ← (Local OCR models used by PaddleOCR)
│
├── whatsapp/ ← Django WhatsApp webhook handler
│ ├── webhook_views.py ← Message flow, button handling, media routing
│ ├── utils.py ← WhatsApp API interaction functions
│ └── urls.py ← Routes to /webhook/
│
├── whatsapp_api_project/ ← Django project settings
│ ├── settings.py
│ └── urls.py
│
├── manage.py ← Django entry point
├── requirements.txt ← Required packages
├── .env ← Environment variables (not committed)
└── .gitignore

💡 Features

    WhatsApp Business API integration

    Interactive button-based flow:

        "Which document do you want to verify?"

        Options: PAN or Aadhaar

        After upload, backend verifies the document via OCR

    PAN/Aadhaar detection & validation using PaddleOCR

    Flask API for document parsing

    Seamless Django <-> Flask communication

    Handles images and PDFs from WhatsApp

⚙️ Setup Instructions

    Clone the repository:

git clone https://github.com/OmMathur23/whatsapp-doc-validator.git
cd whatsapp-doc-validator

    Set up virtual environments:

python3.10 -m venv venv310
source venv310/bin/activate
pip install -r requirements.txt

Note: PaddleOCR models are stored locally in backend/models/ to avoid large downloads.

    Configure your environment variables in .env:

WHATSAPP_ACCESS_TOKEN=your_long_token
WHATSAPP_PHONE_NUMBER_ID=your_number_id
WHATSAPP_API_VERSION=v16.0

    Start Flask OCR API:

cd backend
python app.py

    Start Django server:

cd ..
python manage.py runserver 0.0.0.0:8000

🧪 Testing Locally

    Use Postman to simulate webhook POST requests to http://localhost:8000/webhook/.

    To test the full WhatsApp flow, you must:

        Configure your webhook in Meta Developer Console

        Use a tool like ngrok or Render to expose your Django endpoint

🧠 Future Enhancements

    Add support for other documents (Passport, DL, etc)

    Automatic language detection in OCR

    AI-based fraud detection using signature/morphing analysis

    Integration with document databases or CRMs

🧑‍💻 Author

Om Mathur (@OmMathur23)

Made with ❤️ and PaddleOCR.
