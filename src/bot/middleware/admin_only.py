from typing import Any, Awaitable, Callable
from aiogram import BaseMiddleware
from aiogram.types import Message
from src.config import admins_id


class AdminOnly(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: dict[str, Any],
    ) -> Any:
        data["new_value"] = "hello world"
        print(1)
        if event.from_user.id in admins_id:
            return await handler(event, data)
