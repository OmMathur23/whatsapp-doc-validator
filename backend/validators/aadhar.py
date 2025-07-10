
from backend.ocr_utils import run_ocr, load_image_from_bytes, preprocess_image
import re

def extract_aadhar_number(file_bytes):
    img = load_image_from_bytes(file_bytes)
    img = preprocess_image(img)
    text = run_ocr(img)

    match = re.search(r'\b\d{4}[ \-]?\d{4}[ \-]?\d{4}\b', text)
    if match:
        return match.group(0).replace(" ", "").replace("-", "")
    return None
