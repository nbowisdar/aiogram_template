from aiogram import types as t
from aiogram.fsm.context import FSMContext

from src.bot.data.answers import Answer
from src.bot.data.language import formator, messages
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
        markup = answer.cancel_or_hide_active_order(user_id, order["id"], lang)
        await bot.send_message(
            user_id,
            formator(messages["active_order"][lang], order),
            reply_markup=markup,
        )
