from typing import List, Optional
from datetime import datetime, time, timedelta, date
from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True


class EmployeeCreate(BaseModel):
    id_crm: str
    firstName: str
    secondName: str
    lastName: str
    birthday: date
    passer: int
    passnum: int
    snils: str

    class Config:
        orm_mode = True


class EmployeeResponse(BaseModel):
    id: int
    id_crm: str
    firstName: str
    secondName: str
    lastName: str
    birthday: date
    passer: int
    passnum: int
    snils: str

    class Config:
        orm_mode = True


class CitiesCreate(BaseModel):
    Name: str

    class Config:
        orm_mode = True


class CitiesBase(BaseModel):
    id: str
    Name: str

    class Config:
        orm_mode = True


class Cities(CitiesBase):
    id: int
    office_id: int

    class Config:
        orm_mode = True

class CostsResponse(BaseModel):
    number: str
    BankName: str
    BIK: str
    INN: str
    emp_id: int

    class Config:
        orm_mode = True

class CostsRequest(BaseModel):
    id: int
    number: str
    BankName: str
    BIK: str
    INN: str
    emp_id: int

    class Config:
        orm_mode = True


class BranchOfficesResponce(BaseModel):
    Name: str
    INN: int
    KPP: int
    Adress: str
    office_id: int

    class Config:
        orm_mode = True


class BranchOfficesRequest(BaseModel):
    id: int
    Name: str
    INN: int
    KPP: int
    Adress: str
    office_id: int

    class Config:
        orm_mode = True


class ChildrenRequest(BaseModel):
    firstName: str
    secondName: str
    lastName: str
    birthday: date
    emp_id: int

    class Config:
        orm_mode = True


class ChildrenResponce(BaseModel):
    id: int
    firstName: str
    secondName: str
    lastName: str
    birthday: date
    emp_id: int

    class Config:
        orm_mode = True