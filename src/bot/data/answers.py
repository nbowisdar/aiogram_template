from src.bot.data.language import translations
from src.bot.data.schema import Message_Back

from . import kb_builders

messages = translations["messages"]
buttons = translations["buttons"]


# def _get_buttons()


def _set_buttons_text(btns_text: list[str], lang: str) -> list[str]:
    return [buttons[text][lang] for text in btns_text]


def _set_args_to_text(text: str, data: list[str]) -> str:
    for _, d in enumerate(data):
        text = text.replace("{}", d, 1)
    return text


def _get_info(
    key: str, btns_text: list[str], lang: str, ajust: int, *args
) -> Message_Back:
    ajust = 3
    btns_text = _set_buttons_text(btns_text, lang)
    btn = kb_builders.build_reply_buttons(btns_text, ajust)
    text = messages[key][lang]
    if args:
        text = _set_args_to_text(text, args)
    return Message_Back(text, btn)


def user_main_menu(
    *,
    lang="en",
    canceled=False,
) -> Message_Back:
    ajust = 3

    if canceled:
        key = "cancel"
    else:
        key = "main_menu"
    btns_text = ["balance", "statistics", "market", "help"]
    return _get_info(key, btns_text, lang, ajust)


def user_cancel(lang="en") -> Message_Back:
    ajust = 3
    key = "cancel"
    btns_text = [key]

    return _get_info(key, btns_text, lang, ajust)


def balance(lang="en", *args) -> Message_Back:
    ajust = 2
    key = "balance"
    btns_text = ["deposit", "withdraw", "cancel"]

    return _get_info(key, btns_text, lang, ajust, *args)
