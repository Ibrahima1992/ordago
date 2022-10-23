from pydantic import BaseModel
from datetime import datetime
from typing import Optional

from pydantic.types import conint


class UserOut(BaseModel):
    id: int
    login: str
    created_at: datetime

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    login: str
    password: str


class UserLogin(BaseModel):
    login: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None

