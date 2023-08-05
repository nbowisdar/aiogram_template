import aiogram.types as t
from . import base

cancel_kb = t.ReplyKeyboardMarkup(
    keyboard=[[t.KeyboardButton(text="🛑 Скасувати")]], resize_keyboard=True
)

statistick_btn = t.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            t.InlineKeyboardButton(text="🔰 За добу", callback_data="error_stat|day"),
            t.InlineKeyboardButton(
                text="⌚️ За неділю", callback_data="error_stat|week"
            ),
        ],
        [base.drop_msg],
    ]
)
