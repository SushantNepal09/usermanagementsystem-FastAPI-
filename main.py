from fastapi import FastAPI
from databaseconn import sessionusedtoconnect , engine
import database_models
from pydanticmodelsmadebyme import EmployeePydantic

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


def _init_db():
    db = sessionusedtoconnect()
    
    count = db.query(database_models.Employee).count()
    
    
    if count == 0:
        for loopeduser in users:
            
            db.add(database_models.Employee(**loopeduser.model_dump()))
            
        db.commit()
       


_init_db()


@app.get("/")
def getfunc():
    db = sessionusedtoconnect()
    db.query()
    return users

@app.post("/")
def postfunc(user: str):
    users.append(user)
    return users

@app.put("/{key}")
def updatefun(key:int,new_user: str):
    if key< 0 or key >= len(users):
        return "not found"
    else:
        users[key] = new_user
        return users
    
    

@app.delete("/{key}")
def delfunc(key:int):
    if key < 0 or len(users)<= key:
        return "User not found"
    else:
        del_user = users[key]
        del users[key]
        return {"deleted_user ": del_user}