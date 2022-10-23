from operator import index
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

from pydantic.types import conint


class AutomobileBase(BaseModel):
    company: str
    body_style: str
    wheel_base: float
    length: float
    engine_type: str
    num_of_cylinders: str
    horsepower: int
    average_mileage: float
    price: float


class AutomobileOut(BaseModel):
    index: int

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

    company: Optional[str]
    body_style: Optional[str]
    wheel_base: Optional[float]
    length: Optional[float]
    engine_type: Optional[str]
    num_of_cylinders: Optional[str]
    horsepower: int
    average_mileage: Optional[float]
    price: Optional[float]


class AutoCher(BaseModel):
    company: Optional[str]
    price: Optional[float]


class AutomobileList(BaseModel):
    items: List[AutomobileOut]
    total: int
    page: int
    size: int


class Automobile(AutomobileBase):
    index: int

    class config:
        orm_mode = True


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

