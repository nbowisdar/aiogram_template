from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session

# from app.structure import models
from app.database import get_db

# def get_user

Database = Annotated[Session, Depends(get_db)]
# UserDep = Annotated[models.User, Depends(get_user)]
