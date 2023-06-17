from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import aiogram.types as t
from setup import periods
from config import admins_id

drop_msg = t.InlineKeyboardButton(text="↙️ Приховати", callback_data="hide")

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
        [drop_msg],
    ]
)
