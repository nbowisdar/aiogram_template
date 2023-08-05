import asyncio

from aiogram.types import Message

from .tables import User


class CRUD_User:
    @staticmethod
    async def get_user(id: int) -> User | None:
        return await User.objects().get(User.id == id)

    @staticmethod
    async def get_user_by_chat_id(chat_id: int) -> User | None:
        return await User.objects().get(User.chat_id == chat_id)

    @staticmethod
    async def get_or_create_user_from_msg(msg: Message) -> User:
        return await User.objects().get_or_create(
            User.chat_id == msg.from_user.id,
            defaults={User.username: msg.from_user.username},
        )

    @staticmethod
    async def delete_user(chat_id: int):
        await User.delete().where(User.chat_id == chat_id)


crud_user = CRUD_User()


async def test():
    user = await crud_user.get_user_by_chat_id(123)


if __name__ == "__main__":
    asyncio.run(test())
