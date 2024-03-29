import aiogram.types as t
from aiogram.utils.keyboard import InlineKeyboardBuilder

# from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from src.bot.data.schema import Text_Data

drop_msg = t.InlineKeyboardButton(text="↙️ Приховати", callback_data="hide")


def build_reply_buttons(buttons_text: list[str], adjast: int) -> t.ReplyKeyboardMarkup:
    buttons = [t.KeyboardButton(text=text) for text in buttons_text]
    builder = ReplyKeyboardBuilder()
    builder.add(*buttons)
    builder.adjust(adjast)

    return builder.as_markup(resize_keyboard=True)


def build_reply_buttons_strict(buttons_text: list[list[str]]) -> t.ReplyKeyboardMarkup:
    kb = [
        list(map(lambda btns_raw: t.KeyboardButton(text=btns_raw), btns_raw))
        for btns_raw in buttons_text
    ]
    return t.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )


def build_inline_kb(data: list[Text_Data], adjust=1) -> t.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for d in data:
        builder.button(text=d.text, callback_data=d.callback_data)
    builder.adjust(adjust)
    return builder.as_markup()

# def build_inline_kb_strict(data: list[Text_Data]) -> t.InlineKeyboardMarkup:
#     builder = InlineKeyboardBuilder()
#     for d in data:
#         builder.button(text=d.text, callback_data=d.callback_data)
#     builder.adjust(adjast)
#     return builder.as_markup()
