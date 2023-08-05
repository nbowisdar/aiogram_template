from src.bot.data.language import translations
from src.bot.data.schema import Message_Back

from . import kb_builders

msgs = translations["messages"]
btns = translations["buttons"]


# def _get_buttons()


def _get_info(key: str, btns_text: list[str], lang="en", ajust=4) -> Message_Back:
    btn = kb_builders.build_reply_buttons(btns_text, ajust)
    text = msgs[key][lang]
    return Message_Back(text, btn)


def user_main_menu(*, lang="en", canceled=False, ajust=4) -> Message_Back:
    if canceled:
        key = "cancel"
    else:
        key = "main_menu"
    btns_text = ["balance", "statistics", "market", "help"]
    return _get_info(key, btns_text, lang, ajust)


def user_cancel(lang="en", ajust=4) -> Message_Back:
    # key = msgs["cancel"][lang]
    key = "cancel"
    btns_text = [key]

    return _get_info(key, btns_text, lang, ajust)
