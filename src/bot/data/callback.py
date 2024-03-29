from aiogram.filters.callback_data import CallbackData

"""Call Back data"""


class Trade_Menu(CallbackData, prefix="trade_menu"):
    user_id: int
    action: str


class Confirm_New_Order(CallbackData, prefix="confirm_new_order"):
    user_id: int
    action: str


class Cancel_Active_Order(CallbackData, prefix="cancel_hide_order"):
    user_id: int
    action: str
    order_id: int
