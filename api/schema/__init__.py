from pydantic import BaseModel, IPvAnyAddress


class ListAuto(BaseModel):
    autos: dict


class ListNbCar(BaseModel):
    company: str
    nb_cars: int


class AvgNbCar(BaseModel):
    company: str
    avg_by_company: float


class ListCarPrice(BaseModel):
    company: str
    price: float
