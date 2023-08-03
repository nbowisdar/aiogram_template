from pprint import pprint
from aiogram.filters.callback_data import CallbackData

import aiogram.types as t
from aiogram.utils.keyboard import ReplyKeyboardBuilder

drop_msg = t.InlineKeyboardButton(text="↙️ Приховати", callback_data="hide")


def build_reply_buttons(buttons_text: list[str], adjast=4) -> t.ReplyKeyboardMarkup:
    buttons = [t.KeyboardButton(text=text) for text in buttons_text]
    builder = ReplyKeyboardBuilder()
    builder.add(*buttons)
    builder.adjust(adjast)
    return builder.as_markup()


def get_keyboard_fab(data: list[tuple], adjast=4) -> t.InlineKeyboardMarkup:
    builder = t.InlineKeyboardBuilder()
    for text, callback_data in data:
        builder.add(t.InlineKeyboardButton(text=text, callback_data=callback_data))
    builder.adjust(4)
    return builder.as_markup()
