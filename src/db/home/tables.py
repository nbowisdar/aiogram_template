from datetime import datetime

from piccolo.columns import (
    BigInt,
    Boolean,
    Float,
    Integer,
    Timestamp,
    Varchar,
    ForeignKey,
)
from piccolo.table import Table


class User(Table, tablename="users"):
    chat_id = BigInt(unique=True)
    username = Varchar()
    balance = Float(default=0.0)
    reg_date = Timestamp(default=datetime.now)
    lang = Varchar(default="en", length=10)
    # ban = Integer(default=0)
    # bonus = Float(default=0)
    # bonus_on_id = Float(default=0)
    # transaction_data = Varchar(default="")


class Order(Table):
    # active = IntegerField(default=1)
    status = Varchar(default="active")
    seller = ForeignKey(references=User)
    buyer = ForeignKey(references=User)
    date = Timestamp(default=datetime.now)
    status = Varchar(default="active")
    amount_sell = Float()
    amount_receive = Float()


# class P2P_User(Table, tablename="p2p_users"):
#     chat_id = BigInt()
#     name = Varchar(null=True)
#     ban = Integer(default=0)
#     successful = Float(null=True)
#     arbitration = Float(null=True)
#     dontpay = Float(null=True)
#     date = Timestamp(default=datetime.now)


# class P2P_Order(Table):
#     # active = IntegerField(default=1)
#     status = Varchar(default="active")
#     chat_id_sell = BigInt()
#     seller_name = Varchar(null=True)
#     chat_id_buy = BigInt(null=True)
#     buyer_name = Varchar(null=True)
#     card = Varchar(null=True)
#     bank = Varchar(null=True)
#     amount_sell = Float(null=True)
#     amount_receive = Float(null=True)
#     persent = Float(null=True)
#     date = Timestamp(default=datetime.now)
#     msg_id = BigInt(null=True)


# class Task(Table):
#     """
#     An example table.
#     """

#     name = Varchar()
#     completed = Boolean(default=False)
