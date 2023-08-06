import aiogram.types as t
from aiogram import F, filters
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

# from src.bot.data import answers
from src.bot.data.answers import Answer, buttons, messages
from src.bot.setup import user_router
from src.bot.utils.cache import Cache
from src.db.home.crud import CRUD_User
from src.db.home.tables import User

crud_user = CRUD_User()
cache = Cache()
answer = Answer()


@user_router.message(F.text.in_(buttons["cancel"].values()))
async def cancel_handler(message: t.Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    user = await cache.get_user(message)
    if current_state is None:
        info = answer.user_main_menu(user.lang)
    else:
        await state.clear()
        info = answer.user_main_menu(canceled=True)

    await message.answer(info.text, reply_markup=info.kb)


@user_router.message(filters.Command(commands="start"))
async def main(message: t.Message):
    user = await cache.get_user(message)
    info = answer.user_main_menu(lang=user.lang)
    await message.answer(info.text, reply_markup=info.kb)


@user_router.message(F.text.in_(buttons["balance"].values()))
async def balance(message: t.Message):
    user = await cache.get_user(message)
    info = answer.balance(user.lang, str(user.balance))
    await message.answer(info.text, reply_markup=info.kb)


@user_router.message(F.text.in_(buttons["trade"].values()))
async def trade_menu(message: t.Message):
    user = await cache.get_user(message)
    info = answer.trade_menu_inline(user.lang)
    await message.answer(info.text, reply_markup=info.kb)


@user_router.message(F.text == "test")
async def test(message: t.Message):
    await message.answer("bot works")
