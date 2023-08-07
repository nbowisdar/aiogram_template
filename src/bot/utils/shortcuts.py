from aiogram import types as t
from aiogram.fsm.context import FSMContext


async def get_lang_from_state(state: FSMContext) -> str:
    data = await state.get_data()
    return data["lang"]
