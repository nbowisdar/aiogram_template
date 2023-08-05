import aiogram.filters as f
import aiogram.types as t
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from src.bot.data import answers
from src.bot.setup import admin_router


@admin_router.message(f.Command(commands="admin"))
async def test(message: t.Message):
    text, btns = answers.admin_main()
    await message.answer(text, reply_markup=btns)
