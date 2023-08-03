from sqlalchemy.orm import Session
from src.data import models, schemas
from .database import auto_commit


@auto_commit()
def get_user(id: int, db: Session) -> models.User | None:
    return db.get(models.User, id)


@auto_commit()
def get_users(db: Session) -> models.User | None:
    return db.query(models.User).all()


@auto_commit(commit=True)
def create_user(user: schemas.User_Create, db: Session) -> models.User | None:
    db.add(models.User(**user.model_dump()))


@auto_commit(commit=True)
def delete_user(id: int, db: Session) -> bool:
    deleted = db.query(models.User).filter(models.User.id == id).delete()
    if deleted:
        return True
    return False
