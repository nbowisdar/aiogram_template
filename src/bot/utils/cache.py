from aiogram.types import Message

from src.db.home import crud
from src.db.home.tables import User
from src.logger import logger


class Cache:
    def __init__(self) -> None:
        self.users = {}
        self.user_crud = crud.CRUD_User()

    async def _create_and_save_user(self, msg: Message) -> User:
        user = await self.user_crud.get_or_create_user_from_msg(msg)
        if user._was_created:
            logger.info(f"New user - {user.username}")
        logger.debug(f"[User] {user.username}: saved to cache")
        self.users[msg.from_user.id] = user
        return user

    async def get_user(self, msg: Message) -> User:
        # get_user_from_cache, or create and save new one
        user = self.users.get(msg.from_user.id)
        if user:
            logger.debug(f"[User] {user.username}: found in cache")
            return user
        return await self._create_and_save_user(msg)

    async def get_user_by_id(self, user_id: int) -> User:
        return self.users.get(user_id)
