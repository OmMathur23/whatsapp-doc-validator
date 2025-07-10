from backend.ocr_utils import run_ocr, load_image_from_bytes, preprocess_image
import re

def extract_pan_number(file_bytes):
    img = load_image_from_bytes(file_bytes)
    img = preprocess_image(img)
    text = run_ocr(img)

    pan_match = re.search(r'([A-Z]{5}[0-9]{4}[A-Z])', text)
    if pan_match:
        return pan_match.group(1)
    return None
