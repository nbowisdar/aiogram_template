from typing import NamedTuple

from aiogram import types
from aiogram.filters.callback_data import CallbackData

# from abc import ABC, abstractmethod

# from typing import Protocol


# class Button_Builder_Base(ABC):
#     @abstractmethod
#     def _set_text_to_buttons(btns_text: list, lang: str) -> list[str]:
#         """Set appropriate text to buttons"""
#         pass

#     @abstractmethod
#     def build_answer(
#         cls, key: str, btns_text: list[str], lang: str, ajust: int = 3, args=[]
#     ):
#         pass


class Text_Data(NamedTuple):
    text: str
    callback_data: CallbackData


class Message_Back(NamedTuple):
    text: str
    kb: types.InlineKeyboardMarkup | types.ReplyKeyboardMarkup


# class NumbersCallbackFactory(CallbackData, prefix="fabnum"):
#     action: str
#     value: int | None = None


# x = NumbersCallbackFactory(action="action", value=2)
