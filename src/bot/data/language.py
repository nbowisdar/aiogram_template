import json
from typing import Iterable

from src.config import language_file_path

with open(language_file_path, "r", encoding="utf-8") as f:
    translations = json.load(f)

messages = translations["messages"]


def build_message_with_values(key: str, lang: str, values: Iterable) -> str:
    values = list(map(str, values))
    msg: str = messages[key][lang]
    for v in values:
        msg = msg.replace("{}", v, 1)
    return msg


def insert_dect_in_text(text: str, d: dict) -> str:
    print(d)
    for k, v in d.items():
        text = text.replace(f"${k}", str(v))
    return text


def build_msg_with_values_from_dict(key: str, lang: str, d: dict) -> str:
    msg: str = messages[key][lang]
    return insert_dect_in_text(msg, d)
