from sqlalchemy.orm import Session
from src.data import models
from src.bot import deps


def get_user(id: int, db: deps.Database) -> models.User | None:
    return db.get(models.User, id)
