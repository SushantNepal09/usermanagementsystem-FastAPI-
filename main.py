from fastapi import FastAPI
from databaseconn import sessionusedtoconnect , engine
import database_models


app = FastAPI()

database_models.Base.metadata.create_all(bind = engine)

users = []

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