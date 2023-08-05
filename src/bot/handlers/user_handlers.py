import aiogram.types as t
from aiogram import F, filters
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

# from src.bot.buttons import user_btn as answers
from src.bot.data import answers
from src.bot.data.answers import buttons, messages

# from src.bot.data.language import translations
from src.bot.setup import user_router
from src.bot.utils.cache import Cache

# from src.db.home.crud import crud_user
# from src.db.home.crud import crud_user
from src.db.home.crud import CRUD_User
from src.db.home.tables import User

crud_user = CRUD_User()
cache = Cache()


@user_router.message(F.text.in_(buttons["cancel"].values()))
async def cancel_handler(message: t.Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        text, kb = answers.user_main_menu()
    else:
        await state.clear()
        text, kb = answers.user_main_menu(canceled=True)

    await message.answer(text, reply_markup=kb)


@user_router.message(filters.Command(commands="start"))
async def main(message: t.Message):
    user = await cache.get_user(message)
    text, kb = answers.user_main_menu(lang=user.lang)
    await message.answer(text, reply_markup=kb)


@user_router.message(F.text == "test")
async def test(message: t.Message):
    await message.answer("bot works")
