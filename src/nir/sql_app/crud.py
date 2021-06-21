from sqlalchemy.orm import Session

from . import models, schemas
from typing import (List, Optional)


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def create_employee(db: Session, emp: schemas.EmployeeCreate):
    db_emp = models.Employee(**emp.dict())
    db.add(db_emp)
    db.commit()
    db.refresh(db_emp)
    return db_emp


# def create_employee(db: Session, emp: schemas.EmployeeCreate):
#     db_emp = models.Employee(id_crm=emp.id_crm, firstName=emp.firstName, secondName=emp.secondName,
#                              lastName=emp.lastName,
#                              birthday=emp.birthday, passer=emp.passer, passnum=emp.passer, snils=emp.snils)
#     db.add(db_emp)
#     db.commit()
#     db.refresh(db_emp)
#     return db_emp

def get_emp(db: Session, skip: int = 0, limit: int = 100) -> Optional[models.Employee]:
    return db.query(models.Employee).offset(skip).limit(limit).all()


def put_employee(id: int, db: Session, emp: schemas.EmployeeCreate):
    emp_put = db.query(models.Employee).filter(models.Employee.id == id).one_or_none()

    if emp_put is None:
        return None

    for var, value in vars(emp).items():
        setattr(emp_put, var, value) if value else None

    db.add(emp_put)
    db.commit()
    db.refresh(emp_put)
    return emp_put


def delete_cost_by_id(db: Session, id: int) -> Optional[models.Costs]:
    cost_del = db.query(models.Costs).filter(models.Costs.id == id).one_or_none()

    if cost_del is None:
        return None

    db.delete(cost_del)
    db.commit()
    # db.refresh(cost_del)
    return {"message": "DROP STRING"}


def delete_city_by_id(db: Session, id: int) -> Optional[models.Cities]:
    city_del = db.query(models.Cities).filter(models.Cities.id == id).one_or_none()

    if city_del is None:
        return None

    db.delete(city_del)
    db.commit()
    # db.refresh(cost_del)
    return {"message": "DROP STRING"}


def get_emp_by_id(db: Session, id: int) -> Optional[models.Employee]:
    emp = (db
           .query(models.Employee)
           .filter(models.Employee.id == id)
           .first())
    # emp_child_id = (db
    #        .query(models.Employee)
    #        .filter(models.Employee.id).first()) == db.query(models.Childes.emp_id)
    #                 .first())
    # emp_child = (db
    #              .query(models.Childes)
    #              .filter(models.Childes.id == emp_child_id)
    #              .first())
    return emp #, emp_child


def create_cities(db: Session, city: schemas.CitiesCreate):
    db_city = models.Cities(**city.dict())
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city


def get_cities(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Cities).offset(skip).limit(limit).all()


def get_city_by_id(db: Session, id: int) -> Optional[models.Cities]:
    city = (db
            .query(models.Cities)
            .filter(models.Cities.id == id)
            .first())
    return city


def get_cost_by_id(db: Session, id: int) -> Optional[models.Costs]:
    cost = (db
            .query(models.Costs)
            .filter(models.Costs.id == id)
            .first())
    return cost


def create_office_cities(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def create_costs(db: Session, cost: schemas.CostsResponse):
    db_cost = models.Costs(**cost.dict())
    db.add(db_cost)
    db.commit()
    db.refresh(db_cost)
    return db_cost


def create_office(db: Session, office: schemas.BranchOfficesResponce):
    db_office = models.BranchOffices(**office.dict())
    db.add(db_office)
    db.commit()
    db.refresh(db_office)
    return db_office


def get_offices(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.BranchOffices).offset(skip).limit(limit).all()

def delete_office_by_id(db: Session, id: int) -> Optional[models.BranchOffices]:
    office_del = db.query(models.BranchOffices).filter(models.BranchOffices.id == id).one_or_none()

    if office_del is None:
        return None

    db.delete(office_del)
    db.commit()
    # db.refresh(cost_del)
    return {"message": "DROP STRING"}


def put_office(id: int, db: Session, office: schemas.BranchOfficesRequest):
    office_put = db.query(models.BranchOffices).filter(models.BranchOffices.id == id).one_or_none()

    if office_put is None:
        return None

    for var, value in vars(office).items():
        setattr(office_put, var, value) if value else None

    db.add(office_put)
    db.commit()
    db.refresh(office_put)
    return office_put


def create_child(db: Session, child: schemas.ChildrenResponce):
    db_child = models.Childes(**child.dict())
    db.add(db_child)
    db.commit()
    db.refresh(db_child)
    return db_child


def get_childs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Childes).offset(skip).limit(limit).all()


def put_child(id: int, db: Session, child: schemas.ChildrenResponce):
    child_put = db.query(models.Childes).filter(models.Childes.id == id).one_or_none()

    if child_put is None:
        return None

    for var, value in vars(child).items():
        setattr(child_put, var, value) if value else None

    db.add(child_put)
    db.commit()
    db.refresh(child_put)
    return child_put