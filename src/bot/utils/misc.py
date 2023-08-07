from aiogram import types as t
from aiogram.fsm.context import FSMContext

from src.bot.data.language import messages, formator
from src.bot.setup import bot
from src.config import admins_id
from src.logger import logger


def get_status_symbol(b: bool) -> str:
    if b:
        return "🟢"
    return "🔴"


url = "https://www.google.com/"


async def send_warning(msg: str, user_id: int, send_to_admin=True):
    await bot.send_message(user_id, msg)
    if send_to_admin:
        await bot.send_message(admins_id[0], msg)
    logger.debug("Warning was sent")


def divide_big_msg(msg: str) -> list[str]:
    if len(msg) < 4000:
        return [msg]

    return msg.split("\n\n")
