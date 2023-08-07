import aiogram.types as t
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.bot.data import callback, schema
from src.bot.data.language import formator, translations
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
# callback_buttons = translations["inline_buttons"]


class Answer_Builder_Base:
    @staticmethod
    def _set_args_to_text(text: str, data: list[str]) -> str:
        for _, d in enumerate(data):
            text = text.replace("{}", d, 1)
        return text

    # @staticmethod
    # def _set_args_to_text(text: str, data: list[str]) -> str:
    #     for _, d in enumerate(data):
    #         text = text.replace("{}", d, 1)
    #     return text


class Answer_Builder(Answer_Builder_Base):
    @staticmethod
    def _set_buttons_text(btns_text: list[str], lang: str) -> list[str]:
        print(btns_text)
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
            resp.append(buttons[key][lang])
        return resp

    def build_kb(
        self,
        *,
        callbac_data: CallbackData,
        btns_text: tuple[str],
        values_list: tuple[dict],
        lang: str,
        ajust: int = 1,
    ) -> t.InlineKeyboardMarkup | t.ReplyKeyboardMarkup:
        # get buttons text on the selected language
        btns_text = self._set_buttons_text(btns_text, lang)

        # create list of callback data and text
        text_data_list = self.inner_builder.build_inline_kb_bulk(
            callbac_data, btns_text, values_list
        )
        # create keyboard
        return build_inline_kb(text_data_list, ajust)

    def build_answer(
        self,
        callbac_data: CallbackData,
        key: str,
        btns_text: tuple[str],
        values_list: tuple[dict],
        lang: str,
        ajust: int = 1,
        data={},
    ) -> Message_Back:
        btn = self.build_kb(
            callbac_data=callbac_data,
            btns_text=btns_text,
            values_list=values_list,
            lang=lang,
            ajust=ajust,
        )

        text = messages[key][lang]
        # set args to text
        if data:
            text = formator(text, data)
        return Message_Back(text, btn)

        # # get buttons text on the selected language
        # btns_text = self._set_buttons_text(btns_text, lang)  ######
        # # btns_text = self._set_buttons_text_strict(btns_text, lang)  ######

        # # create list of callback data and text
        # text_data_list = self.inner_builder.build_inline_kb_bulk(
        #     callbac_data, btns_text, values_list
        # )
        # # create keyboard
        # btn = build_inline_kb(text_data_list, ajust)

        # Need to sepparate that


"""Buttons"""
main_menu_btn = [["balance", "trade", "statistics"], ["help"]]

"""Inline Buttons"""
confirm_cancel_btn = "confirm", "cancel"
cancel_hide_btn = "hide", "cancel"


class Answer:
    def __init__(
        self,
    ) -> None:
        self.builder = Answer_Builder()
        self.strict_builder = Answer_Builder_Strict()
        self.inline_builder = Answer_Builder_Inline()

    def user_cancel(self, lang="en") -> Message_Back:
        key = "canceled"
        btns_text = [key]

        return self.builder.build_answer(key, btns_text, lang)

    def confirmed(self, lang="en") -> Message_Back:
        key = "confirmed"
        # btns_text = [key]

        return self.strict_builder.build_answer(key, main_menu_btn, lang)

    def user_main_menu(self, *, lang="en", canceled=False) -> Message_Back:
        key = "cancel" if canceled else "main_menu"

        return self.strict_builder.build_answer(key, main_menu_btn, lang)

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

        return self.inline_builder.build_answer(
            callback.Trade_Menu, key, texts, values, lang
        )

    def confirm_new_order(self, user_id: int, data: dict, lang="en") -> Message_Back:
        key = "confirm_new_order"
        texts = "confirm", "cancel"
        values = (
            {"action": "confirm", "user_id": user_id},
            {"action": "cancel", "user_id": user_id},
        )

        return self.inline_builder.build_answer(
            callback.Confirm_New_Order, key, texts, values, lang, data=data
        )

    def cancel_or_hide_active_order(
        self, user_id: int, order_id: int, lang="en"
    ) -> t.InlineKeyboardMarkup:
        ajust = 2

        values = (
            {"action": "hide", "order_id": order_id, "user_id": user_id},
            {"action": "cancel", "order_id": order_id, "user_id": user_id},
        )

        return self.inline_builder.build_kb(
            callbac_data=callback.Cancel_Active_Order,
            btns_text=cancel_hide_btn,
            values_list=values,
            lang=lang,
            ajust=ajust,
        )
