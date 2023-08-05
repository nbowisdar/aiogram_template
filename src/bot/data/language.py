import json

from src.config import language_file_path

with open(language_file_path, "r", encoding="utf-8") as f:
    translations = json.load(f)
