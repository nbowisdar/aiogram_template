from typing import Iterable, TypeVar

import aiogram.types as t

from src.bot.data.language import translations, build_message
from src.bot.data import schema

from .kb_builders import (
    build_inline_kb,
    build_reply_buttons,
    build_reply_buttons_strict,
)

messages = translations["messages"]
buttons = translations["buttons"]


# callback_buttons = translations["inline_buttons"]


# class Answer_Builder_Base:
#     @staticmethod
#     def _set_args_to_text(text: str, data: list[str]) -> str:
#         for _, d in enumerate(data):
#             text = text.replace("{}", d, 1)
#         return text

# @staticmethod
# def _set_args_to_text(text: str, data: list[str]) -> str:
#     for _, d in enumerate(data):
#         text = text.replace("{}", d, 1)
#     return text


class Markup:
    @staticmethod
    def _set_buttons_text(btns_text: list[str], lang: str) -> list[str]:
        return [buttons[text][lang] for text in btns_text]

    @classmethod
    def buttons(cls, data: schema.Answer_Build_Data) -> t.ReplyKeyboardMarkup:
        btns_text = cls._set_buttons_text(data.btns_text, data.lang)
        adj = 1 if not data.adjust else data.adjust
        return build_reply_buttons(btns_text, adj)


class Markup_Strict:
    @staticmethod
    def _set_buttons_text(btns_list: list[list[str]], lang: str) -> list[list[str]]:
        new_list = []
        for btns_row in btns_list:
            new_list.append([buttons[text][lang] for text in btns_row])
        return new_list

    @classmethod
    def buttons(cls, data: schema.Answer_Build_Data) -> t.ReplyKeyboardMarkup:
        btns_text = cls._set_buttons_text(data.btns_text, data.lang)
        return build_reply_buttons_strict(btns_text)


class Markup_Inline:

    @staticmethod
    def _set_buttons_text(btns_text: Iterable[str], lang: str) -> list[str]:
        return [buttons[key][lang] for key in btns_text]

    @classmethod
    def buttons(cls, data: schema.Answer_Build_Data_Inline) -> t.InlineKeyboardMarkup:
        # create list of callback data and text
        builder = schema.Text_Data_Builder(data.callback_data)

        # localize text for buttons
        btns_text = cls._set_buttons_text(data.btns_text, data.lang)

        text_data_list = builder.bulk_build_text_data(btns_text, data.values_list)
        # create keyboard
        return build_inline_kb(text_data_list, data.adjust)

    # def build_answer(
    #         self,
    #         callback_data: CallbackData,
    #         btns_text: Iterable[str],
    #         values_list: Iterable[dict],
    #         adjust: int = 1,
    #
    # ) -> MessageDate:
    #     markup = self.buttons(
    #         callback_data=callback_data,
    #         btns_text=btns_text,
    #         values_list=values_list,
    #         adjust=adjust,
    #     )

    # set args to text
    # if data:
    #     text = inject_args(text, data)
    # return MessageDate(text, btn)

    # # get buttons text on the selected language

    # # create list of callback data and text
    # text_data_list = self.inner_builder.build_inline_kb_bulk(
    #     callbac_data, btns_text, values_list
    # )
    # # create keyboard
    # btn = build_inline_kb(text_data_list, adjust)

    # Need to sepparate that


Answer_Data = TypeVar('Answer_Data',
                      schema.Answer_Build_Data_Dict,
                      schema.Answer_Build_Data_Inline_Dict,
                      schema.Answer_Build_Data,
                      schema.Answer_Build_Data_Inline)


class Answer:
    def __init__(self):
        # self.builder = Answer_Builder()
        self._simple_builder = Markup()
        self._strict_builder = Markup_Strict()
        self._inline_builder = Markup_Inline()

    @staticmethod
    def _from_dict_to_tuple(
            data: schema.Answer_Build_Data_Dict | schema.Answer_Build_Data_Inline_Dict
    ) -> schema.Answer_Build_Data | schema.Answer_Build_Data_Inline:

        if data.get("callback_data"):
            return schema.Answer_Build_Data_Inline(**data)
        else:
            return schema.Answer_Build_Data(**data)

    def generate_answer(self, data: Answer_Data,
                        builder: schema.AnswerEnum = schema.AnswerEnum.STRICT) -> schema.MessageDate:
        if isinstance(data, dict):
            data = self._from_dict_to_tuple(data)
        match builder:
            case schema.AnswerEnum.SIMPLE:
                reply_markup = self._simple_builder.buttons(data)
            case schema.AnswerEnum.STRICT:
                reply_markup = self._strict_builder.buttons(data)
            case schema.AnswerEnum.INLINE:
                reply_markup = self._inline_builder.buttons(data)
            case _:
                raise Exception("Wrong builder")
        text = build_message(data.text_key, data.lang, data.injection)
        return schema.MessageDate(text=text, reply_markup=reply_markup)

    # def confirmed(self, lang="en") -> MessageDate:
    #     key = "confirmed"
    #     # btns_text = [key]
    #
    #     return self.strict_builder.build_answer(key, main_menu_btn, lang)
    #

    #
    # def confirm_new_order(self, user_id: int, data: dict, lang="en") -> MessageDate:
    #     key = "confirm_new_order"
    #     texts = "confirm", "cancel"
    #     values = (
    #         {"action": "confirm", "user_id": user_id},
    #         {"action": "cancel", "user_id": user_id},
    #     )
    #
    #     return self.inline_builder.build_answer(
    #         callback.Confirm_New_Order, key, texts, values, lang, data=data
    #     )
    #
    # def cancel_or_hide_active_order(
    #     self, user_id: int, order_id: int, lang="en"
    # ) -> t.InlineKeyboardMarkup:
    #     adjust = 2
    #
    #     values = (
    #         {"action": "hide", "order_id": order_id, "user_id": user_id},
    #         {"action": "cancel", "order_id": order_id, "user_id": user_id},
    #     )
    #
    #     return self.inline_builder.build_kb(
    #         callbac_data=callback.Cancel_Active_Order,
    #         btns_text=cancel_hide_btn,
    #         values_list=values,
    #         lang=lang,
    #         adjust=adjust,
    #     )
