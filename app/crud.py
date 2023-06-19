from sqlalchemy.orm import Session
from app.structure import models
from app import deps


def get_user(id: int, db: deps.Database) -> models.User | None:
    return db.get(models.User, id)
