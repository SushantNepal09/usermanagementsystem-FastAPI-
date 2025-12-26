from fastapi import FastAPI,Depends
from databaseconn import sessionusedtoconnect , engine
import database_models
from pydanticmodelsmadebyme import EmployeePydantic
from sqlalchemy.orm import Session

app = FastAPI()

database_models.Base.metadata.create_all(bind = engine)



users = [
  EmployeePydantic(
    id=1,
    name="Sushant11",
    address="Itahari, Sunsari",
    salary=10000000,
    contractyears=4,
    contact=9812121211
),

EmployeePydantic(
    id=2,
    name="Aarav",
    address="Dharan, Sunsari",
    salary=8500000,
    contractyears=3,
    contact=9801122334
),

EmployeePydantic(
    id=3,
    name="Rohan",
    address="Biratnagar, Morang",
    salary=9200000,
    contractyears=5,
    contact=9845678901
),

EmployeePydantic(
    id=4,
    name="Nishant",
    address="Kathmandu",
    salary=12000000,
    contractyears=4,
    contact=9861234567
),

EmployeePydantic(
    id=5,
    name="Prakash",
    address="Pokhara, Kaski",
    salary=7800000,
    contractyears=2,
    contact=9819988776
),

EmployeePydantic(
    id=6,
    name="Bikash",
    address="Lalitpur",
    salary=8800000,
    contractyears=3,
    contact=9804455667
),

EmployeePydantic(
    id=7,
    name="Anish",
    address="Butwal, Rupandehi",
    salary=8300000,
    contractyears=4,
    contact=9843344556
),

EmployeePydantic(
    id=8,
    name="Suman",
    address="Hetauda, Makwanpur",
    salary=9000000,
    contractyears=3,
    contact=9822233344
)

    
    
    
]

def get_db():
    db = sessionusedtoconnect()
    try:
        yield db
    finally:
        db.close()









def _init_db():
    db = sessionusedtoconnect()
    
    count = db.query(database_models.Employee).count()
    
    
    if count == 0:
        for loopeduser in users:
            
            db.add(database_models.Employee(**loopeduser.model_dump()))
            
        db.commit()
       


_init_db()


@app.get("/")
def getfunc(db: Session = Depends(get_db)):
  db_values =   db.query(database_models.Employee).all()
  return db_values

@app.get("/employee/{key}")
def get_id(id:int,db: Session = Depends(get_db)):
    db_value = db.query(database_models.Employee).filter(database_models.Employee.id == id).first()
    if db_value:
        return db_value
    return "Product Not Found"


@app.post("/")
def postfunc(user: EmployeePydantic, db: Session = Depends(get_db)):
    db.add(database_models.Employee(**user.model_dump()))
    db.commit()
    return user

@app.put("/")
def updatefun(id:int,new_user: EmployeePydantic,db : Session = Depends(get_db)):
    db_values = db.query(database_models.Employee).filter(database_models.Employee.id == id).first()
    if db_values:
        db_values.name = new_user.name
        db_values.address = new_user.address
        db_values.contact = new_user.contact
        db_values.contractyears = new_user.contractyears
        db_values.salary = new_user.salary
        db.commit()
        return "Product Updated"
    else:
        return "Product Not Found"
    
    
    

@app.delete("/")
def del_products(id:int,db:Session = Depends(get_db)):
    db_values = db.query(database_models.Employee).filter(database_models.Employee.id == id).first()
    if db_values:
        db.delete(db_values)
        db.commit()
        return "Deleted"
    else:
        return "not found"
