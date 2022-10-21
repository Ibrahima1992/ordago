import email
from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    lastname: str
    firstname: str
    login: str
    email: str
    password: str

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    email: Optional[str]


class UserLogin(BaseModel):
    login: str
    password: str


class UserUpdateOut(BaseModel):
    email: str


class UserOut(BaseModel):
    id: int
    lastname: Optional[str]
    firstname: Optional[str]
    login: Optional[str]
    email: Optional[str]

    class Config:
        orm_mode = True


class User(UserBase):
    id: int

    class config:
        orm_mode = True

    lastname: Optional[str]
    firstname: Optional[str]
    login: Optional[str]
    email: Optional[str]
