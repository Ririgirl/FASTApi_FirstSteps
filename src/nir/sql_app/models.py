from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, time, timedelta

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")


class Employee(Base):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True, index=True)
    id_crm = Column(String, unique=True)
    firstName = Column(String)
    secondName = Column(String)
    lastName = Column(String)
    birthday = Column(Date)
    passer = Column(Integer)
    passnum = Column(Integer)
    snils = Column(String)

class Costs(Base):
    __tablename__ = "costs"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(String, unique=True)
    BankName = Column(String)
    BIK = Column(String)
    INN = Column(String)
    emp_id = Column(Integer, ForeignKey("employee.id"))


class Childes(Base):
    __tablename__ = "childes"

    id = Column(Integer, primary_key=True, index=True)
    firstName = Column(String)
    secondName = Column(String)
    lastName = Column(String)
    birthday = Column(Date)
    emp_id = Column(Integer, ForeignKey("employee.id"))

class Contracts(Base):
    __tablename__ = "contracts"

    id = Column(Integer, primary_key=True, index=True)
    firstName = Column(String)
    secondName = Column(String)
    lastName = Column(String)
    birthday = Column(Date)
    number = Column(String)
    secondName = Column(String)
    lastName = Column(String)
    datecontract = Column(Date)
    emp_id = Column(Integer, ForeignKey("employee.id"))


class Cities(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    Name = Column(String)


class BranchOffices(Base):
    __tablename__ = "branchOffices"

    id = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    INN = Column(Integer)
    KPP = Column(Integer)
    Adress = Column(String)
    office_id = Column(Integer, ForeignKey("cities.id"))


