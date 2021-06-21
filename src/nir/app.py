from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime, time, timedelta

from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from .sql_app import crud, models, schemas
from .sql_app.database import SessionLocal, engine

from .sql_app.models import Employee

tags_metadata = [
    {
        'name': 'NIR_Employee',
        'description': 'Поиск, получение, изменение, удаление и добавление данных по сотруднику',
    },
    {
        'name': 'NIR_Costs',
        'description': 'Поиск, получение, изменение, удаление и добавление данных по счетам сотрудника',
    },
    {
        'name': 'NIR_Cities',
        'description': 'Поиск, получение, изменение, удаление и добавление данных по городам',
    },
    {
        'name': 'NIR_Offices',
        'description': 'Поиск, получение, изменение, удаление и добавление данных по офисам',
    },
    {
        'name': 'NIR_Childs',
        'description': 'Поиск, получение, изменение, удаление и добавление данных по детям сотрудников',
    },
    {
        'name': 'Test',
        'description': 'Тестовые примеры',
    }
]

app = FastAPI(
    title='NIR_API',
    description='Сервис принятия и обработки данных',
    version='1.0.0',
    openapi_tags=tags_metadata,
)


# models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class FoundEmp(BaseModel):
    firstName: Optional[str] = None
    secondName: Optional[str] = None
    lastName: Optional[str] = None
    birthday: Optional[datetime] = None


class passportEmp(BaseModel):
    number: Optional[int]
    series: Optional[int]


class foundEmpResponse(BaseModel):
    id_crm: str
    firstName: Optional[str]
    secondName: Optional[str]
    lastName: Optional[str]
    birthday: Optional[datetime]


class PostResponceScheme(BaseModel):
    Employee: foundEmpResponse = None
    Passport: passportEmp = None


@app.post('/crm/', response_model=PostResponceScheme, tags=['Test'])
def emp_list_post(emp: FoundEmp, pasp: Optional[passportEmp] = None):
    return {
        'employee': {f'id_crm': {}, 'count': 4, 'size': None},
        'bars': [
            {'apple': 'x1', 'banana': 'y'},
            {'apple': 'x2', 'banana': 'y'},
        ],
    }


@app.get('/crm/{id}', tags=['Test'])
def emp_list_get(id: str):
    return {"message": f'{id}'}


@app.get("/test", tags=['Test'])
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}", tags=['Test'])
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.post("/users/", response_model=schemas.User, tags=['Test'])
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User], tags=['Test'])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/employee/", response_model=List[schemas.EmployeeCreate], tags=['NIR_Employee'])
def read_emp(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    emp = crud.get_emp(db, skip=skip, limit=limit)
    return emp


@app.post('/employee/', response_model=schemas.EmployeeResponse, tags=['NIR_Employee'])
def emp_list_post(emp: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db=db, emp=emp)


@app.put('/employee/', response_model=schemas.EmployeeResponse, tags=['NIR_Employee'])
def emp_list_post(id: int, emp: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.put_employee(id=id, db=db, emp=emp)


@app.get("/employee/{id}",  tags=['NIR_Employee'])
def read_emp_by_id(id: int, db: Session = Depends(get_db)):
    emp_und = crud.get_emp_by_id(db, id=id)
    return emp_und


@app.post('/cities/', response_model=schemas.CitiesBase, tags=['NIR_Cities'])
def city_list_post(city: schemas.CitiesCreate, db: Session = Depends(get_db)):
    return crud.create_cities(db=db, city=city)


@app.get("/cities/{id}", response_model=schemas.CitiesBase, tags=['NIR_Cities'])
def read_city_by_id(id: int, db: Session = Depends(get_db)):
    city = crud.get_city_by_id(db, id=id)
    return city


@app.get("/costs/{id}", response_model=schemas.CostsResponse, tags=['NIR_Costs'])
def read_cost_by_id(id: int, db: Session = Depends(get_db)):
    cost = crud.get_cost_by_id(db, id=id)
    return cost


@app.post('/costs/', response_model=schemas.CostsRequest, tags=['NIR_Costs'])
def create_costs(cost: schemas.CostsResponse, db: Session = Depends(get_db)):
    return crud.create_costs(db=db, cost=cost)


@app.get("/cities/", response_model=List[schemas.CitiesBase], tags=['NIR_Cities'])
def read_cities(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    cities = crud.get_cities(db, skip=skip, limit=limit)
    return cities


@app.delete("/cost/{id}", tags=['NIR_Costs'])
def delete_cost_by_id(id: int, db: Session = Depends(get_db)):
    return crud.delete_cost_by_id(db=db, id=id)
    #return {"message": "DROP THIS"}


@app.delete("/city/{id}", tags=['NIR_Cities'])
def delete_city_by_id(id: int, db: Session = Depends(get_db)):
    return crud.delete_city_by_id(db=db, id=id)


@app.post('/office/', response_model=schemas.BranchOfficesRequest, tags=['NIR_Offices'])
def create_office(office: schemas.BranchOfficesResponce, db: Session = Depends(get_db)):
    return crud.create_office(db=db, office=office)


@app.get("/offices/", response_model=List[schemas.BranchOfficesResponce], tags=['NIR_Offices'])
def read_offices(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    offices = crud.get_offices(db, skip=skip, limit=limit)
    return offices


@app.delete("/office/{id}", tags=['NIR_Offices'])
def delete_office_by_id(id: int, db: Session = Depends(get_db)):
    return crud.delete_office_by_id(db=db, id=id)


@app.put('/office/', response_model=schemas.BranchOfficesRequest, tags=['NIR_Offices'])
def put_office(id: int, office: schemas.BranchOfficesResponce, db: Session = Depends(get_db)):
    return crud.put_office(id=id, db=db, office=office)


@app.post('/child/', response_model=schemas.ChildrenResponce, tags=['NIR_Childs'])
def create_child(child: schemas.ChildrenRequest, db: Session = Depends(get_db)):
    return crud.create_child(db=db, child=child)


@app.get("/childs/", response_model=List[schemas.ChildrenRequest], tags=['NIR_Childs'])
def get_childs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    childs = crud.get_childs(db, skip=skip, limit=limit)
    return childs

@app.put('/childs/{id}', response_model=schemas.ChildrenRequest, tags=['NIR_Childs'])
def put_child(id: int, child: schemas.ChildrenRequest, db: Session = Depends(get_db)):
    return crud.put_child(id=id, db=db, child=child)

