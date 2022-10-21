from sqlalchemy import Column, Integer, String, Float
from config import Base

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


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
    __tablename__ = "t_user"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    lastname = Column(String(50), nullable=False)
    firstname = Column(String(50), nullable=False)
    login = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False)
    password = Column(String(), nullable=False)

    @classmethod
    def add_user(cls, db, data):
        data = data.dict()
        new_user = cls(**data)
        db.add(new_user)
        db.flush()
        db.commit()
        db.refresh(new_user)

        return new_user

    @classmethod
    def update_user(cls, db, id, data):
        user_in = cls.user_by_id(db=db, id=id)

        if user_in:
            data = data.__dict__
            db.query(cls).filter(cls.id == id).update(data)
            db.commit()
            return user_in
        else:
            return user_in

    @classmethod
    def user_by_id(cls, db, id):
        return db.query(cls).get(id)

    @classmethod
    def user_by_name(cls, db, login):
        return db.query(cls).filter(cls.login.like(str(login))).first()

    @classmethod
    def get_user_by_mail(cls, db, mail):
        return db.query(cls).filter(cls.email.like(str(mail))).first()


class Hasher:
    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password):
        return pwd_context.hash(password)
