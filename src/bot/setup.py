from pathlib import Path

from aiogram import Bot, Dispatcher, Router
from aiogram.fsm.storage.memory import MemoryStorage

from src.config import settings

bot = Bot(settings.token_bot, parse_mode="MARKDOWN")

storage = MemoryStorage()

dp = Dispatcher(storage=storage)

# create routes
admin_router = Router()
user_router = Router()
