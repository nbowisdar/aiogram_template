from aiogram.fsm.context import FSMContext
import aiogram.filters as f
from aiogram import F
import app.structure.models

from setup import user_router
import aiogram.types as t
from app.buttons import user_btn as kb
from app import crud
from aiogram.fsm.state import State, StatesGroup
from app import msgs, utils


@user_router.message(F.text.in_(["🔴 Скасувати", "↩️ Назад"]))
async def cancel_handler(message: t.Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        await message.answer("🏡 Головна", reply_markup=kb.user_main_kb)
        return
    await state.clear()
    await message.answer("🔴 Скасованно", reply_markup=kb.user_main_kb)


@user_router.message(f.Command(commands="start"))
async def main(message: t.Message):
    await message.answer("🏡 Головна", reply_markup=kb.user_main_kb)


@user_router.message(F.text == "test")
async def test(message: t.Message):
    await message.answer("bot works")
