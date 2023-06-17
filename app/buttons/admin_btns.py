import aiogram.types as t
from app import utils


drop_msg = t.InlineKeyboardButton(text="↙️ Приховати", callback_data="hide")

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
        [
            t.InlineKeyboardButton(
                text="🗓 За місяць", callback_data="error_stat|month"
            ),
            t.InlineKeyboardButton(
                text="🌎 За 3 місяці", callback_data="error_stat|3months"
            ),
            # t.InlineKeyboardButton(
            #     text="📊 Уся статистика", callback_data="new_user_stat|all_new_user_stat"
            # ),
        ],
        [drop_msg],
    ]
)
