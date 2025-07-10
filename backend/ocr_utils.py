
import os
import cv2
import numpy as np
from paddleocr import PaddleOCR
from PIL import Image
import io

BASE = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE, "models")

ocr = PaddleOCR(
    use_angle_cls=True,
    lang='en',
    det_model_dir=os.path.join(MODEL_DIR, 'en_ppocr_mobile_v2.0_det_infer'),
    rec_model_dir=os.path.join(MODEL_DIR, 'en_ppocr_mobile_v2.0_rec_infer'),
    cls_model_dir=os.path.join(MODEL_DIR, 'ch_ppocr_mobile_v2.0_cls_infer')
)

def load_image_from_bytes(b: bytes) -> Image.Image:
    try:
        return Image.open(io.BytesIO(b)).convert("RGB")
    except:
        from pdf2image import convert_from_bytes
        return convert_from_bytes(b, dpi=300)[0].convert("RGB")

def preprocess_image(img: Image.Image) -> np.ndarray:
    arr = np.array(img)
    gray = cv2.cvtColor(arr, cv2.COLOR_RGB2GRAY)
    eq = cv2.equalizeHist(gray)
    bgr = cv2.cvtColor(eq, cv2.COLOR_GRAY2BGR)
    upscaled = cv2.resize(bgr, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)
    return upscaled

def run_ocr(img) -> str:
    result = ocr.ocr(img, cls=True)
    lines = [line[1][0] for block in result for line in block]
    return "\n".join(lines)
