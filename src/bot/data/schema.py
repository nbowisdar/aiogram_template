from typing import NamedTuple, TypedDict, Iterable
from enum import Enum, auto
from aiogram import types
from aiogram.filters.callback_data import CallbackData

"""Enums"""


class AnswerBuilder(Enum):
    SIMPLE = auto()
    STRICT = auto()
    INLINE = auto()


"""Other schema"""


class Text_Data(NamedTuple):
    text: str
    callback_data: CallbackData


class Answer_Build_Data(NamedTuple):
    text_key: str
    btns_text: list[list[str]] | list[str]
    lang: str
    injection: dict | None = None
    adjust: int = None


class Answer_Build_Data_Inline(NamedTuple):
    text_key: str
    btns_text: list[list[str]] | list[str]
    lang: str
    values_list: Iterable[dict]
    callback_data: CallbackData
    injection: dict | None = None
    adjust: int = None


class Answer_Build_Data_Dict(TypedDict):
    text_key: str
    btns_text: list[list[str]] | list[str]
    lang: str
    injection: dict | None = None
    adjust: int = None


class Answer_Build_Data_Inline_Dict(Answer_Build_Data_Dict):
    values_list: Iterable[dict]
    callback_data: CallbackData


class MessageDate(TypedDict):
    text: str
    reply_markup: types.InlineKeyboardMarkup | types.ReplyKeyboardMarkup


"""helper builders"""


class Text_Data_Builder:
    def __init__(self, callback_data: CallbackData) -> None:
        self.callback_data = callback_data

    def build_text_data(self, text: str, values: dict) -> Text_Data:
        return Text_Data(text, self.callback_data(**values))

    def bulk_build_text_data(
            self, texts: Iterable[str], values_list: Iterable[dict]
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
            callback_data: CallbackData, btns_text: Iterable[str], values_list: Iterable[dict]
    ) -> list[Text_Data]:
        local_builder = Text_Data_Builder(callback_data)
        return local_builder.bulk_build_text_data(btns_text, values_list)
