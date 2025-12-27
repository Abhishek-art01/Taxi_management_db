import pytesseract
from pdf2image import convert_from_path
import pandas as pd

# --- PATHS (adjust only if yours are different) ---
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
POPPLER_PATH = r"C:\poppler-25.12.0\Library\bin"

PDF_FILE = "scanned.pdf"
OUTPUT_EXCEL = "output.xlsx"

# --- Convert PDF to images ---
images = convert_from_path(
    PDF_FILE,
    dpi=300,
    poppler_path=POPPLER_PATH
)

data = []

# --- OCR each page ---
for img in images:
    text = pytesseract.image_to_string(img, lang="eng")

    for line in text.split("\n"):
        if line.strip():
            # Split by multiple spaces (better for tables)
            row = line.split()
            data.append(row)

# --- Save to Excel ---
df = pd.DataFrame(data)
df.to_excel(OUTPUT_EXCEL, index=False)

print("✅ DONE! Excel file created:", OUTPUT_EXCEL)
