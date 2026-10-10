"""Compare extracted PDF text, ignoring visual spacing and Unicode variants."""
from difflib import SequenceMatcher
from pathlib import Path
import logging
import unicodedata

import pdfplumber

logging.disable(logging.CRITICAL)
ROOT = Path(__file__).resolve().parent


def read_pdf(path):
    with pdfplumber.open(path) as pdf:
        return "\n".join(page.extract_text() or "" for page in pdf.pages), len(pdf.pages)


def normalize(text):
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("〜", "~")
    text = text.translate(str.maketrans({"⻘": "青", "⻜": "飞", "⻆": "角", "戶": "户", "⻅": "见", "⻔": "门"}))
    return "".join(char for char in text if not char.isspace() and char != "•")


original, original_pages = read_pdf(ROOT / "刘元智 (18).pdf")
result, result_pages = read_pdf(ROOT / "刘元智_简历.pdf")
old, new = normalize(original), normalize(result)
print(f"Original: {original_pages} pages; result: {result_pages} pages")
if old == new:
    print("PASS: Full text matches after spacing and Unicode normalization.")
else:
    for tag, i, j, a, b in SequenceMatcher(None, old, new, autojunk=False).get_opcodes():
        if tag != "equal":
            print(f"{tag}: original={old[i:j]!r}; result={new[a:b]!r}")
    raise SystemExit(1)
