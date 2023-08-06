import asyncio

from src.bot.handlers.admin_handlers import admin_router
from src.bot.handlers.user_handlers import user_router
from src.bot.middleware.admin_only import AdminOnly
from src.bot.setup import bot, dp
from src.logger import logger


async def _start():
    admin_router.message.middleware(AdminOnly())
    dp.include_router(admin_router)
    dp.include_router(user_router)

    await dp.start_polling(bot)


def start_simple():
    asyncio.run(_start())


def main():
    # args = parser.parse_args()
    try:
        # if args.admin:
        #     logger.debug("Bot started with admin pannel")
        #     execute_in_background(start_admin)
        logger.debug("Bot started")
        start_simple()
    except KeyboardInterrupt:
        logger.info("Bot stopped by admin")


if __name__ == "__main__":
    main()
