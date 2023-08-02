import aiogram.types as t
from aiogram import F, filters
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from src.bot import misc, msgs
from src.bot.buttons import user_btn as kb
from src.bot.db import crud
from src.bot.setup import user_router


@user_router.message(F.text.in_(["🔴 Скасувати", "↩️ Назад"]))
async def cancel_handler(message: t.Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        await message.answer("🏡 Головна", reply_markup=kb.user_main_kb)
        return
    await state.clear()
    await message.answer("🔴 Скасованно", reply_markup=kb.user_main_kb)


@user_router.message(filters.Command(commands="start"))
async def main(message: t.Message):
    await message.answer("🏡 Головна", reply_markup=kb.user_main_kb)


@user_router.message(F.text == "test")
async def test(message: t.Message):
    await message.answer("bot works")
