from typing import NamedTuple, TypedDict
from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
