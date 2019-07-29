from sqlalchemy import Column, Integer, String, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Application(Base):
	__tablename__ = "Application"
	id = Column(Integer, primary_key=True)
	name = Column(String)
	email = Column(String)
	phone = Column(String)
	adress=Column(String)

class volunteer(Base):
	__tablename__ = "volunteer"
	id = Column(Integer, primary_key=True)
	vol_mail = Column(String)
	
