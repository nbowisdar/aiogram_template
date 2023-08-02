import aiogram.types as t
from aiogram.types import InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from . import base

_cancel = t.KeyboardButton(text="🔴 Скасувати")

cancel_kb = t.ReplyKeyboardMarkup(
    keyboard=[[t.KeyboardButton(text="🔴 Скасувати")]], resize_keyboard=True
)


user_main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📝 Button"),
            KeyboardButton(text="📜 Button2"),
        ],
        [KeyboardButton(text="Inline response")],
    ],
    resize_keyboard=True,
)


test_inl = t.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            t.InlineKeyboardButton(text="♻️ Оновити", callback_data=f"prefix|action"),
            t.InlineKeyboardButton(text="🗑 Видалити", callback_data=f"prefix|action"),
        ],
        [base.drop_msg],
    ]
)
