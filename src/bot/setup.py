from pathlib import Path
from aiogram import Bot, Dispatcher, Router
from src.config import settings

bot = Bot(settings.token_bot, parse_mode="MARKDOWN")
dp = Dispatcher()

# create routes
admin_router = Router()
user_router = Router()
