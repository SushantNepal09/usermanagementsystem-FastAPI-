from pydantic import BaseModel

class EmployeePydantic(BaseModel):
    id:int
    name:str
    address: str
    salary: int
    contractyears: int
    contact:int