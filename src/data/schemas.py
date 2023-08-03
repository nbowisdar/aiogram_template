from typing import NamedTuple, TypedDict

from pydantic import BaseModel


class User_Create(BaseModel):
    username: str


class User(User_Create):
    username: str
    status: str
