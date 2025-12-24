from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = "postgresql://postgres:sushantsql@localhost:5432/employeetable"
engine = create_engine(db_url)
sessionusedtoconnect = sessionmaker(autoflush=False,bind= engine,autocommit = False)