from typing import NamedTuple

from aiogram import types
from aiogram.filters.callback_data import CallbackData




"""Other schema"""


class Text_Data(NamedTuple):
    text: str
    callback_data: CallbackData


class Message_Back(NamedTuple):
    text: str
    kb: types.InlineKeyboardMarkup | types.ReplyKeyboardMarkup


"""helper builders"""


class Text_Data_Builder:
    def __init__(self, callback_data: CallbackData) -> None:
        self.callback_data = callback_data

    def build_text_data(self, text: str, values: dict) -> Text_Data:
        return Text_Data(text, self.callback_data(**values))

    def bulk_build_text_data(
        self, texts: list[str], values_list: list[dict]
    ) -> list[Text_Data]:
        return [
            self.build_text_data(text, values)
            for text, values in zip(texts, values_list)
        ]


class Inline_Builder:
    @staticmethod
    def build_inline_kb(
        callback_data: CallbackData, text: str, values: dict
    ) -> Text_Data:
        local_builder = Text_Data_Builder(callback_data)
        return local_builder.build_text_data(text, values)

    @staticmethod
    def build_inline_kb_bulk(
        callback_data: CallbackData, texts: list[str], values_list: list[dict]
    ) -> list[Text_Data]:
        local_builder = Text_Data_Builder(callback_data)
        return local_builder.bulk_build_text_data(texts, values_list)
