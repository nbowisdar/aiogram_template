from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from piccolo.columns.base import OnDelete
from piccolo.columns.base import OnUpdate
from piccolo.columns.column_types import BigInt
from piccolo.columns.column_types import Float
from piccolo.columns.column_types import ForeignKey
from piccolo.columns.column_types import Timestamp
from piccolo.columns.column_types import Varchar
from piccolo.columns.defaults.timestamp import TimestampNow
from piccolo.columns.indexes import IndexMethod
from piccolo.table import Table


class User(Table, tablename="users", schema=None):
    id = BigInt(
        default=0,
        null=False,
        primary_key=True,
        unique=False,
        index=False,
        index_method=IndexMethod.btree,
        choices=None,
        db_column_name=None,
        secret=False,
    )


ID = "2023-08-07T15:29:48:969353"
VERSION = "0.119.0"
DESCRIPTION = ""


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="home", description=DESCRIPTION
    )

    manager.add_table(
        class_name="User", tablename="users", schema=None, columns=None
    )

    manager.add_table(
        class_name="Order", tablename="order", schema=None, columns=None
    )

    manager.add_column(
        table_class_name="User",
        tablename="users",
        column_name="id",
        db_column_name="id",
        column_class_name="BigInt",
        column_class=BigInt,
        params={
            "default": 0,
            "null": False,
            "primary_key": True,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
    )

    manager.add_column(
        table_class_name="User",
        tablename="users",
        column_name="username",
        db_column_name="username",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 255,
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
    )

    manager.add_column(
        table_class_name="User",
        tablename="users",
        column_name="balance",
        db_column_name="balance",
        column_class_name="Float",
        column_class=Float,
        params={
            "default": 0.0,
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
    )

    manager.add_column(
        table_class_name="User",
        tablename="users",
        column_name="reg_date",
        db_column_name="reg_date",
        column_class_name="Timestamp",
        column_class=Timestamp,
        params={
            "default": TimestampNow(),
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
    )

    manager.add_column(
        table_class_name="User",
        tablename="users",
        column_name="lang",
        db_column_name="lang",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 10,
            "default": "en",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
    )

    manager.add_column(
        table_class_name="Order",
        tablename="order",
        column_name="amount_sell",
        db_column_name="amount_sell",
        column_class_name="Float",
        column_class=Float,
        params={
            "default": 0.0,
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
    )

    manager.add_column(
        table_class_name="Order",
        tablename="order",
        column_name="percent",
        db_column_name="percent",
        column_class_name="Float",
        column_class=Float,
        params={
            "default": 0.0,
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
    )

    manager.add_column(
        table_class_name="Order",
        tablename="order",
        column_name="buyer",
        db_column_name="buyer",
        column_class_name="ForeignKey",
        column_class=ForeignKey,
        params={
            "references": User,
            "on_delete": OnDelete.cascade,
            "on_update": OnUpdate.cascade,
            "target_column": None,
            "null": True,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
    )

    manager.add_column(
        table_class_name="Order",
        tablename="order",
        column_name="seller",
        db_column_name="seller",
        column_class_name="ForeignKey",
        column_class=ForeignKey,
        params={
            "references": User,
            "on_delete": OnDelete.cascade,
            "on_update": OnUpdate.cascade,
            "target_column": None,
            "null": True,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
    )

    manager.add_column(
        table_class_name="Order",
        tablename="order",
        column_name="status",
        db_column_name="status",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 255,
            "default": "active",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
    )

    manager.add_column(
        table_class_name="Order",
        tablename="order",
        column_name="date",
        db_column_name="date",
        column_class_name="Timestamp",
        column_class=Timestamp,
        params={
            "default": TimestampNow(),
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
    )

    return manager
