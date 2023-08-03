import aiogram.types as t
from sqlalchemy.orm import Session

from src.data import models

from .database import get_db


def get_user_by_id(id: int) -> models.User | None:
    db = get_db()
    return db.get(models.User, id)


def get_users() -> models.User | None:
    db = get_db()

    return db.query(models.User).all()


def create_user(user: models.User) -> models.User:
    db = get_db()
    db.add(models.User(**user.model_dump()))


def delete_user(id: int) -> bool:
    db = get_db()
    deleted = db.query(models.User).filter(models.User.id == id).delete()
    if deleted:
        return True
    return False


def get_or_create_user_from_msg(message: t.Message) -> models.User:
    # with get_db() as session:
    db = get_db()
    user = db.query(models.User).filter(models.User.id == message.from_user.id).first()
    if user:
        return user
    user = models.User(id=message.from_user.id, username=message.from_user.username)
    db.add(user)
    db.commit()
    return user
