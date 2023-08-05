import aiogram.types as t
from aiogram import F, filters
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from src.bot.buttons import user_btn as kb
from src.bot.db.language import translations
from src.bot.setup import user_router

# from src.db.home.crud import crud_user
from src.db.test123 import crud_user


@user_router.message(F.text.in_(["🔴 Скасувати", "↩️ Назад"]))
async def cancel_handler(message: t.Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        await message.answer("🏡 Головна", reply_markup=kb.user_main_kb)
        return
    await state.clear()
    await message.answer("🔴 Скасованно", reply_markup=kb.user_main_kb)


# @user_router.message(filters.Command(commands="start"))
# async def main(message: t.Message):
#     user = crud.get_or_create_user_from_msg(message)
#     await message.answer(translations[user.lang]["start"], reply_markup=kb.user_main_kb)


@user_router.message(filters.Command(commands="test"))
async def main(message: t.Message):
    user = await crud_user.get_user_by_chat_id(message.from_user.id)
    if user:
        msg = f"Hello {user.username}, You are already registered"
    else:
        msg = "Preale register first"
    await message.answer(msg)


@user_router.message(F.text == "test")
async def test(message: t.Message):
    await message.answer("bot works")
