import aiogram.types as t
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.bot.data import schema
from src.bot.data.language import translations
from src.bot.data.schema import (
    Inline_Builder,
    Message_Back,
    Text_Data,
)

from .kb_builders import (
    build_inline_kb,
    build_reply_buttons,
    build_reply_buttons_strict,
)

messages = translations["messages"]
buttons = translations["buttons"]
callback_buttons = translations["inline_buttons"]


class Answer_Builder_Base:
    @staticmethod
    def _set_args_to_text(text: str, data: list[str]) -> str:
        for _, d in enumerate(data):
            text = text.replace("{}", d, 1)
        return text


class Answer_Builder(Answer_Builder_Base):
    @staticmethod
    def _set_buttons_text(btns_text: list[str], lang: str) -> list[str]:
        return [buttons[text][lang] for text in btns_text]

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


class Answer_Builder_Strict(Answer_Builder_Base):
    @staticmethod
    def _set_buttons_text(btns_list: list[list[str]], lang: str) -> list[str]:
        new_list = []
        for btns_row in btns_list:
            new_list.append([buttons[text][lang] for text in btns_row])
        return new_list

    @classmethod
    def build_answer(
        cls, key: str, btns_text: list[str], lang: str, args=[]
    ) -> Message_Back:
        btns_text = cls._set_buttons_text(btns_text, lang)
        # build kb using builder and ajust
        btn = build_reply_buttons_strict(btns_text)
        text = messages[key][lang]
        if args:
            text = cls._set_args_to_text(text, args)
        return Message_Back(text, btn)


class Answer_Builder_Inline(Answer_Builder_Base):
    def __init__(self) -> None:
        self.inner_builder = Inline_Builder()

    @staticmethod
    def _set_buttons_text(btns_text: list[str], lang: str) -> list[str]:
        resp = []
        for key in btns_text:
            resp.append(callback_buttons[key][lang])
        return resp

    def build_answer(
        self,
        callbac_data: CallbackData,
        key: str,
        btns_text: tuple[str],
        values_list: tuple[dict],
        lang: str,
        ajust: int = 1,
        args=[],
    ) -> Message_Back:
        # get buttons text on the selected language
        btns_text = self._set_buttons_text(btns_text, lang)

        # create list of callback data and text
        text_data_list = self.inner_builder.build_inline_kb_bulk(
            callbac_data, btns_text, values_list
        )
        # create keyboard
        btn = build_inline_kb(text_data_list, ajust)
        text = messages[key][lang]
        # set args to text
        if args:
            text = self._set_args_to_text(text, args)
        return Message_Back(text, btn)


class Answer:
    def __init__(
        self,
    ) -> None:
        self.builder = Answer_Builder()
        self.strict_builder = Answer_Builder_Strict()
        self.inline_builder = Answer_Builder_Inline()

    def user_main_menu(self, *, lang="en", canceled=False) -> Message_Back:
        key = "cancel" if canceled else "main_menu"

        btns_text = [["balance", "trade", "statistics"], ["help"]]
        return self.strict_builder.build_answer(key, btns_text, lang)

    def user_cancel(self, lang="en") -> Message_Back:
        key = "cancel"
        btns_text = [key]

        return self.builder.build_answer(key, btns_text, lang)

    def balance(self, lang="en", *args) -> Message_Back:
        key = "balance"
        btns_text = [["deposit", "withdraw"], ["cancel"]]
        return self.strict_builder.build_answer(key, btns_text, lang, *args)

    def trade_menu_inline(self, user_id: int, lang="en") -> Message_Back:
        key = "trade_menu"
        texts = "new_trade", "buy_coin", "my_trades"
        values = (
            {"action": "new_trade", "user_id": user_id},
            {"action": "buy_coin", "user_id": user_id},
            {"action": "my_trades", "user_id": user_id},
        )

        msg_back = self.inline_builder.build_answer(
            schema.Trade_Menu_CallbackData, key, texts, values, lang
        )
        return msg_back
