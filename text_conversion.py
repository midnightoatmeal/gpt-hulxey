from pypdf import PdfReader
from pathlib import Path

pdf_path =  "users/midnight_oatmeal/Desktop/huxley_essays.pdf"
out_txt = "huxley_raw.txt"

reader = PdfReader(pdf_path)
with open(out_txt, "w", encoding="utf-8") as f:
    for i, page in enumerate(reader.pages, 1):
        text = page.extract_text() or ""
        f.write(text.strip() + "\n\n<<<PAGEBREAK>>>\n\n")
print(f"Wrote {out_txt}")