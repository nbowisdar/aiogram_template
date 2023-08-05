from typing import NamedTuple
from aiogram import types
from aiogram.filters.callback_data import CallbackData


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
