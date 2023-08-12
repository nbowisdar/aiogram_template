from aiogram import types as t
from aiogram.fsm.context import FSMContext

from src.bot.data import callback
from src.bot.data.answers import Answer
from src.bot.data.language import inject_args, messages
from src.bot.data.schema import Answer_Build_Data_Inline_Dict, AnswerEnum
from src.bot.setup import bot
from src.db.home.crud import CRUD_Order, CRUD_User

crud_user = CRUD_User()
crud_order = CRUD_Order()
# cache = Cache()
answer = Answer()


async def get_lang_from_state(state: FSMContext) -> str:
    data = await state.get_data()
    return data["lang"]


async def send_users_active_trades(user_id: int, lang: str) -> list:
    orders = await crud_order.get_users_orders(user_id)
    if not orders:
        return await bot.send_message(user_id, messages["no_active_orders"][lang])
    for order in orders:
        order["created_at"] = order["created_at"].strftime("%d.%m.%Y %H:%M")

        data: Answer_Build_Data_Inline_Dict = {
            "adjust": 2, "injection": None,

            "text_key": "active_order",
            "btns_text": ["new_trade", "buy_coin", "my_trades"],
            "values_list": [
                {"action": "hide", "order_id": order["id"], "user_id": user_id},
                {"action": "cancel", "order_id": order["id"], "user_id": user_id},
            ],
            "lang": lang,
            "callback_data": callback.Cancel_Active_Order
        }
        resp = answer.generate_answer(data, AnswerEnum.INLINE)

        await bot.send_message(
            user_id,
            resp["text"],
            reply_markup=resp["reply_markup"],
        )


async def send_users_active_trades(user_id: int, lang: str) -> list:
    orders = await crud_order.get_users_orders(user_id)
    if not orders:
        return await bot.send_message(user_id, messages["no_active_orders"][lang])
    for order in orders:
        order["created_at"] = order["created_at"].strftime("%d.%m.%Y %H:%M")

        data: Answer_Build_Data_Inline_Dict = {
            "adjust": 2, "injection": {
                "created_at": order["created_at"],
                "amount_sell": order["amount_sell"],
                "percent": order["percent"],
            },

            "text_key": "active_order",
            "btns_text": ["hide", "cancel"],
            "values_list": [
                {"action": "hide", "order_id": order["id"], "user_id": user_id},
                {"action": "cancel", "order_id": order["id"], "user_id": user_id},
            ],
            "lang": lang,
            "callback_data": callback.Cancel_Active_Order
        }
        resp = answer.generate_answer(data, AnswerEnum.INLINE)

        await bot.send_message(
            user_id,
            resp["text"],
            reply_markup=resp["reply_markup"],
        )
