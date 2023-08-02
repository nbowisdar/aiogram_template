import aiogram.filters as f
import aiogram.types as t
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from src.bot.buttons import admin_btns as kb
from src.bot.db import crud
from src.bot.setup import admin_router

# from src.bot import msgs, utils


@admin_router.message(F.text.in_(["🛑 Скасувати", "↩️ Назад"]))
async def cancel_handler(message: t.Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        await message.answer("Головна", reply_markup=kb.admin_main_kb)
        return
    await state.clear()
    await message.answer("🛑 Скасованно", reply_markup=kb.admin_main_kb)


@admin_router.callback_query(F.Text("hide"))
async def anon(callback: t.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    if current_state:
        await state.clear()
    await callback.message.delete()


@admin_router.message(f.Command(commands="admin"))
async def test(message: t.Message):
    await message.answer("Головна", reply_markup=kb.admin_main_kb)
