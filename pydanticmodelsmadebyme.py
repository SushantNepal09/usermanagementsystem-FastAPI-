from pydantic import BaseModel

class EmployeePydantic(BaseModel):
    
    name:str
    address: str
    salary: int
    contractyears: int
    contact:int