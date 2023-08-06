from src.bot.data.language import translations
from src.bot.data.schema import Message_Back

from .kb_builders import build_reply_buttons, build_reply_buttons_strict

messages = translations["messages"]
buttons = translations["buttons"]
# print(messages)
# print(buttons)


class Answer_Builder:
    @staticmethod
    def _set_buttons_text(btns_text: list[str], lang: str) -> list[str]:
        return [buttons[text][lang] for text in btns_text]

    @staticmethod
    def _set_buttons_text_strict(btns_list: list[list[str]], lang: str) -> list[str]:
        new_list = []
        for btns_row in btns_list:
            new_list.append([buttons[text][lang] for text in btns_row])
        return new_list

    @staticmethod
    def _set_args_to_text(text: str, data: list[str]) -> str:
        for _, d in enumerate(data):
            text = text.replace("{}", d, 1)
        return text

    @classmethod
    def build_answer(
        cls, key: str, btns_text: list[str], lang: str, ajust: int = 3, args=[]
    ) -> Message_Back:
        btns_text = cls._set_buttons_text(btns_text, lang)
        # build kb using builder and ajust
        btn = build_reply_buttons(btns_text, ajust)
        text = messages[key][lang]
        if args:
            text = cls._set_args_to_text(text, args)
        return Message_Back(text, btn)

    @classmethod
    def build_answer_strict(
        cls, key: str, btns_text: list[str], lang: str, args=[]
    ) -> Message_Back:
        btns_text = cls._set_buttons_text_strict(btns_text, lang)
        # build kb using builder and ajust
        btn = build_reply_buttons_strict(btns_text)
        text = messages[key][lang]
        if args:
            text = cls._set_args_to_text(text, args)
        return Message_Back(text, btn)


class Answer:
    def __init__(self) -> None:
        self.builder = Answer_Builder()

    def user_main_menu(self, *, lang="en", canceled=False) -> Message_Back:
        key = "cancel" if canceled else "main_menu"

        btns_text = [["balance", "statistics", "trade"], ["help"]]
        return self.builder.build_answer_strict(key, btns_text, lang)

    def user_cancel(self, lang="en") -> Message_Back:
        key = "cancel"
        btns_text = [key]

        return self.builder.build_answer(key, btns_text, lang)

    def balance(self, lang="en", *args) -> Message_Back:
        key = "balance"
        btns_text = [["deposit", "withdraw"], ["cancel"]]

        return self.builder.build_answer_strict(key, btns_text, lang, *args)
