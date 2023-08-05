# from typing import Protocol

# class UserCrud(Protocol):
#     @classmethod
#     async def get_user(id: int) -> User | None:
#         return await User.objects().get(User.id == id)

#     @classmethod
#     async def get_user_by_telegram_id(telegram_id: int) -> User | None:
#         return await User.objects().get(User.telegram_id == telegram_id)

#     @classmethod
#     async def get_or_create_user_from_msg(msg: Message) -> User:
#         return await User.objects().get_or_create(
#             User.telegram_id == msg.from_user.id,
#             defaults={User.username: msg.from_user.username},
#         )

#     @classmethod
#     async def delete_user(telegram_id: int):
#         await User.delete().where(User.telegram_id == telegram_id)
