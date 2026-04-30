# utils/text_utils.py
import unicodedata
from pathlib import Path

def utf8_to_ascii_safe(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text)
    return normalized.encode("ascii", "ignore").decode("ascii")

def load_txt_ascii_safe(file_path: str) -> str:
    path = Path(file_path)
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return utf8_to_ascii_safe(f.read())