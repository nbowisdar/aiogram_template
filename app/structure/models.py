from typing import Any
from decimal import Decimal
import sqlalchemy as sa
from sqlalchemy import orm
from datetime import datetime
from app.structure import enums, schemas


class Base(orm.DeclarativeBase):
    created_at: orm.Mapped[datetime] = orm.mapped_column(
        sa.DateTime, default=sa.func.now()
    )


class User(Base):
    __tablename__ = "users"

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    username: orm.Mapped[str] = orm.mapped_column(sa.String(50))
    status: orm.Mapped[str] = orm.mapped_column(
        sa.String(40), default=enums.AccountStatus.CREATED.value
    )


# generic table, can be usefull in some cases
class Proxy(Base):
    __tablename__ = "proxies"

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    name: orm.Mapped[str] = orm.mapped_column(sa.String(100))
    address: orm.Mapped[str] = orm.mapped_column(sa.String(50))
    port: orm.Mapped[int] = orm.mapped_column(sa.Integer)
    login: orm.Mapped[str] = orm.mapped_column(sa.String(50))
    password: orm.Mapped[str] = orm.mapped_column(sa.String(50))

    def build_url(self) -> str:
        return f"http://{self.login}:{self.password}@{self.address}:{self.port}"
