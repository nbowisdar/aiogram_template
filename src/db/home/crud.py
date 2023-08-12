from aiogram.types import Message

from .tables import Order, User

order_id = int


class CRUD_User:
    @staticmethod
    async def get_user(id: int) -> User | None:
        return await User.objects().get(User.id == id)

    # @staticmethod
    # async def get_user_by_chat_id(chat_id: int) -> User | None:
    #     return await User.objects().get(User.chat_id == chat_id)

    @staticmethod
    async def get_or_create_user_from_msg(msg: Message) -> User:
        return await User.objects().get_or_create(
            # User.chat_id == msg.from_user.id,
            User.id == msg.from_user.id,
            defaults={User.username: msg.from_user.username},
        )

    @staticmethod
    async def delete_user(chat_id: int):
        await User.delete().where(User.chat_id == chat_id)


class CRUD_Order:
    @staticmethod
    async def get_order(id: int) -> Order | None:
        return await Order.objects().get(Order.id == id)

    @staticmethod
    async def create_order(amount_sell: float, percent: float, seller_id: int):
        return await Order(
            amount_sell=amount_sell, percent=percent, seller=seller_id
        ).save()

    @staticmethod
    async def delete_order(id: int):
        await Order.delete().where(Order.id == id)

    def get_users_orders(self, user_id: int) -> list[dict]:
        return Order.select().where(Order.seller == user_id)


# crud_user = CRUD_User()


# async def test():
# user = await crud_user.get_user_by_chat_id(123)


# if __name__ == "__main__":
# asyncio.run(test())
