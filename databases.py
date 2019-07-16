
from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///project.db', connect_args={'check_same_thread':False})
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()
	
def add_user_to_database(name, idnum, password, mail):
	singleuser= User(name=name, idnum=idnum, password=password, mail=mail)
	session.add(singleuser)
	session.commit()

def getallusers():
	users=session.query(User).all()
	return users