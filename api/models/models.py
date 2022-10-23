from sqlalchemy import Column, Integer, String, Float
from config import Base
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP


class Automobile(Base):
    __tablename__ = "automobile"

    index = Column(Integer, primary_key=True)
    company = Column(String(50), nullable=False)
    body_style = Column(String(50), nullable=False)
    wheel_base = Column(Float, nullable=False)
    length = Column(Float, nullable=False)
    engine_type = Column(String(), nullable=False)
    num_of_cylinders = Column(String(50), nullable=False)
    horsepower = Column(Integer, nullable=False)
    average_mileage = Column(Float, nullable=False)
    price = Column(Float, nullable=False)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    login = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )

