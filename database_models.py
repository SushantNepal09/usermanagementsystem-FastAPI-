#this is basically creating a model/class which will be turned to the table in database

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String,Integer,Float,Column


Base = declarative_base()

class Employee(Base):
    
    __tablename__ = 'EmployeeInformation'
    id = Column(Integer,primary_key=True,index= True)
    name = Column(String)
    description = Column(String)
    salary = Column(Float)
    contract = Column (Integer)
    
    