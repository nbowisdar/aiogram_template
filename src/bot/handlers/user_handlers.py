import aiogram.types as t
from aiogram import F, filters
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from src.bot.data import callback

# from src.bot.data import answers
from src.bot.data.answers import Answer, buttons, messages
from src.bot.data.language import (
    build_message_with_values,
)
from src.bot.data.schema import Answer_Build_Data, Answer_Build_Data_Inline, Answer_Build_Data_Dict, \
    Answer_Build_Data_Inline_Dict, AnswerEnum
from src.bot.data import schema
from src.bot.setup import user_router
from src.bot.utils import shortcuts as short
from src.bot.utils import validation
from src.bot.utils.cache import Cache
from src.db.home.crud import CRUD_Order, CRUD_User
from src.logger import logger

crud_user = CRUD_User()
crud_order = CRUD_Order()
cache = Cache()
answer = Answer()

"""Buttons"""
main_menu_btn = [["balance", "trade", "statistics"], ["help"]]

"""Inline Buttons"""
confirm_cancel_btn = "confirm", "cancel"
cancel_hide_btn = "hide", "cancel"


@user_router.message(F.text.in_(buttons["cancel"].values()))
async def cancel_handler(message: t.Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    user = await cache.get_user(message)
    if current_state is None:
        key = "canceled"
    else:
        key = "main_menu"
        await state.clear()

    data = Answer_Build_Data(key, main_menu_btn, user.lang)
    response = answer.generate_answer(data)
    await message.answer(**response)


@user_router.message(filters.Command(commands="start"))
async def main(message: t.Message):
    user = await cache.get_user(message)
    key = "main_menu"
    data = Answer_Build_Data(key, main_menu_btn, user.lang)
    response = answer.generate_answer(data)
    await message.answer(**response)


@user_router.message(F.text.in_(buttons["balance"].values()))
async def balance(message: t.Message):
    user = await cache.get_user(message)
    key = "balance"
    btns_text = [["deposit", "withdraw"], ["cancel"]]
    data = Answer_Build_Data(key, btns_text, user.lang)
    response = answer.generate_answer(data)
    await message.answer(**response)


#
@user_router.message(F.text.in_(buttons["trade"].values()))
async def trade_menu(message: t.Message):
    user = await cache.get_user(message)
    data: Answer_Build_Data_Inline_Dict = {
        "adjust": 1, "injection": None,

        "text_key": "trade_menu",
        "btns_text": ["new_trade", "buy_coin", "my_trades"],
        "values_list": [
            {"action": "new_trade", "user_id": user.id},
            {"action": "buy_coin", "user_id": user.id},
            {"action": "my_trades", "user_id": user.id},
        ],
        "lang": user.lang,
        "callback_data": callback.Trade_Menu
    }

    response = answer.generate_answer(data, AnswerEnum.INLINE)
    await message.answer(**response)


@user_router.callback_query(callback.Trade_Menu.filter())
async def handle_trade_menu(
        callback: t.CallbackQuery,
        callback_data: callback.Trade_Menu,
        state: FSMContext,
):
    # msg = callback.message
    user = await cache.get_user_by_id(callback_data.user_id)
    await callback.message.delete()

    match callback_data.action:
        case "new_trade":
            data = Answer_Build_Data("set_amount", ["cancel"], user.lang, injection={"balance": user.balance})
            resp = answer.generate_answer(data, AnswerEnum.SIMPLE)
            await callback.message.answer(**resp)

            await state.set_state(NewOrderState.amount)
            await state.update_data(lang=user.lang)
        case "buy_coin":
            msg = "buy_coin"
        case "my_trades":
            msg = "my_trades"
            await short.send_users_active_trades(user.id, user.lang)


#
# """Creating new order"""
#
#
class NewOrderState(StatesGroup):
    lang = State()
    amount = State()
    percent = State()
    number = State()
    confirm = State()


#
#
@user_router.message(NewOrderState.amount)
async def set_amount(message: t.Message, state: FSMContext):
    amount = validation.simple_check_digit(message.text, float)
    if not amount:
        await message.answer("error")
        return await state.clear()

    await state.update_data(amount=amount)
    await state.set_state(NewOrderState.percent)
    lang = await short.get_lang_from_state(state)
    await message.answer(messages["set_percentage"][lang])


#
#
@user_router.message(NewOrderState.percent)
async def set_percent(message: t.Message, state: FSMContext):
    percent = validation.simple_check_digit(message.text, int)
    if not percent:
        await message.answer("error")
        return await state.clear()

    await state.update_data(percent=percent)
    await state.set_state(NewOrderState.number)
    lang = await short.get_lang_from_state(state)
    await message.answer(messages["set_number"][lang])


#
#
@user_router.message(NewOrderState.number)
async def set_number(message: t.Message, state: FSMContext):
    number = validation.check_mobile_number(message.text)
    if not number:
        await message.answer("error")
        return await state.clear()

    await state.update_data(number=number)
    await state.set_state(NewOrderState.confirm)

    lang = await short.get_lang_from_state(state)
    data = await state.get_data()

    # make answer
    data_resp: Answer_Build_Data_Inline_Dict = {
        "adjust": 1, "injection": data,

        "text_key": "confirm_new_order",
        "btns_text": ["confirm", "cancel"],
        "values_list": [
            {"action": "confirm", "user_id": message.from_user.id},
            {"action": "cancel", "user_id": message.from_user.id}
        ],
        "lang": lang,
        "callback_data": callback.Confirm_New_Order
    }
    resp = answer.generate_answer(data_resp, AnswerEnum.INLINE)

    print(resp)

    await message.answer(**resp)
    # info = answer.confirm_new_order(message.from_user.id, data, lang)

    # await message.answer(info.text, reply_markup=info.kb)


#
#
# @user_router.message(NewOrderState.confirm)
@user_router.callback_query(callback.Confirm_New_Order.filter())
async def confirm_order(
        callback: t.CallbackQuery,
        callback_data: callback.Confirm_New_Order,
        state: FSMContext,
):
    print("confirm")
    await callback.message.delete()
    lang = await short.get_lang_from_state(state)
    data = await state.get_data()
    await state.clear()
    if callback_data.action == "confirm":
        await crud_order.create_order(
            data["amount"], data["percent"], callback_data.user_id
        )
        key = "confirmed"
    else:
        key = "canceled"
    resp = answer.generate_answer(Answer_Build_Data(key, main_menu_btn, lang))
    await callback.message.answer(**resp)


#
@user_router.callback_query(callback.Cancel_Active_Order.filter())
async def cancel_hide_order(
        callback: t.CallbackQuery, callback_data: callback.Cancel_Active_Order
):
    user = await cache.get_user_by_id(callback_data.user_id)
    if callback_data.action == "cancel":
        await crud_order.delete_order(callback_data.order_id)
        await callback.message.edit_text(messages["canceled"][user.lang])
        logger.debug(
            "[User] {} canceled order {}".format(user.username, callback_data.order_id)
        )
    else:
        await callback.message.delete()
#
#
# @user_router.message(F.text == "test")
# async def test(message: t.Message):
#     await message.answer("`bot`works")
