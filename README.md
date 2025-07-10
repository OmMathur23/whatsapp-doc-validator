# WhatsApp Document Validator 📄📲

A WhatsApp-integrated document validation system that leverages OCR to verify official documents like PAN cards, Aadhaar cards, passports, and signatures. Built using Django, Flask, PaddleOCR, and WhatsApp Cloud API.

---

## 🚀 Features

- WhatsApp chatbot interface for users
- OCR-based validation for:
  - PAN Card
  - Aadhaar Card
  - Passport
  - Signature detection
- PDF/Image to text extraction using PaddleOCR and EasyOCR
- REST API endpoints for backend validation
- Media handling and WhatsApp webhook integration
- Deployment-ready with Render support

---

## 🛠️ Tech Stack

- **Frontend/Chat Interface**: WhatsApp Cloud API
- **Backend**:
  - Flask (for OCR APIs)
  - PaddleOCR, EasyOCR, OpenCV, PyTesseract
- **Integration**: Django project to interface WhatsApp with Flask
- **Other**: Postman for testing, Render deployment, `.env` support

---

## 📂 Project Structure

whatsapp-doc-validator/
├── backend/ # Flask OCR backend
│ ├── validators/ # PAN, Aadhaar validators
│ ├── ocr_utils.py # OCR utilities (preprocess, convert, run_ocr)
│ └── app.py # Main Flask app
├── whatsapp/ # WhatsApp integration logic
│ └── utils.py # WhatsApp messaging, media handling
├── whatsapp_api_project/ # Django project
│ └── webhook_views.py # WhatsApp webhook handling
├── manage.py
├── requirements.txt
├── .env
└── .gitignore

---

## 🔄 Flow Overview

1. **User sends "hi" on WhatsApp**
2. **Bot responds with document type buttons**
3. **User selects document type**
4. **Bot prompts file upload**
5. **Media is downloaded and forwarded to Flask backend**
6. **OCR runs validation and returns result**
7. **Bot replies with validation output**

---

## 🧪 API Endpoints (Flask)

- `POST /api/validate/pan`
- `POST /api/validate/aadhar`
- `POST /api/validate/passport`
- [Multipart file upload required; tested via Postman]

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/OmMathur23/whatsapp-doc-validator.git
cd whatsapp-doc-validator

### 2. Create .env file
```
BACKEND_URL=http://127.0.0.1:5000
WHATSAPP_TOKEN=your_whatsapp_token
VERIFY_TOKEN=your_verify_token

### 3. Install Dependencies 
```
pip install -r requirements.txt
