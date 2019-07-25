
from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///project.db', connect_args={'check_same_thread':False})
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()
	
def Add_Application(name, email, phone, adress):
	application= Application(name=name, email=email, phone=phone, adress=adress)
	session.add(application)
	session.commit()

def GetAllApplications():
	applications=session.query(Application).all()
	return applications
