from aiogram.filters.callback_data import CallbackData


class NumbersCallbackFactory(CallbackData, prefix="fabnum"):
    action: str
    value: int | None = None


x = NumbersCallbackFactory(action="action", value=2)
