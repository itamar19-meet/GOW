from sqlalchemy import Column, Integer, String, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Application(Base):
	__tablename__ = "Applications"
	id = Column(Integer, primary_key=True)
	name = Column(String)
	email = Column(String)
	phone_num = Column(Integer)
	
