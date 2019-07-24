
from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///project.db', connect_args={'check_same_thread':False})
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()
	
def Add_Application(name, email, phone_num):
	Application= Applications(name=name, email=email, phone_num=phone_num)
	session.add(Application)
	session.commit()

def GetAllApplications():
	Applications=session.query(Applications).all()
	return Applications
