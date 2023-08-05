import aiogram.types as t
from aiogram import F, filters
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

# from src.bot.buttons import user_btn as answers
from src.bot.data import answers
from src.bot.data.answers import btns, msgs

# from src.bot.data.language import translations
from src.bot.setup import user_router

# from src.db.home.crud import crud_user
from src.db.home.crud import crud_user
from src.db.home.tables import User


@user_router.message(F.text.in_(btns["cancel"].values()))
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
    text, kb = answers.user_main_menu()
    await message.answer(text, reply_markup=kb)


@user_router.message(filters.Command(commands="register"))
async def anon2(message: t.Message):
    user = await crud_user.get_or_create_user_from_msg(message)
    if user._was_created:
        msg = "You registered successfully"
    else:
        msg = "You already registered"
    await message.answer(msg)


@user_router.message(filters.Command(commands=["test"]))
async def anon(message: t.Message):
    user = await crud_user.get_user_by_chat_id(message.from_user.id)
    if user:
        msg = f"Hello {user.username}, You are already registered"
    else:
        msg = "Preale register first"
    await message.answer(msg)


@user_router.message(filters.Command(commands=["drop"]))
async def anon(message: t.Message):
    await crud_user.delete_user(message.from_user.id)

    await message.answer("dropped")


@user_router.message(F.text == "test")
async def test(message: t.Message):
    await message.answer("bot works")
