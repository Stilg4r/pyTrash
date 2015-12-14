#!/usr/bin/env python

import os 
import argparse
from shutil import move
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from createdb import Base, Trashdb
from datetime import date, timedelta,datetime

import config

if not os.path.isdir(".trash"):
	os.makedirs(".trash")

if not os.path.exists(config.dbpath):
	execfile("createdb.py")

engine = create_engine(config.db)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

parser = argparse.ArgumentParser()
parser.add_argument("files", nargs='*')
results = parser.parse_args()

for torm in results.files:
	if os.path.exists(torm):
		if os.path.exists(".trash/"+torm):
			ntorm=torm+"-"+str(datetime.now().microsecond)
			move(torm,".trash/"+ntorm)
			trash=Trashdb(path=os.path.dirname(os.path.realpath(torm))+"/.trash/"+ntorm,expiration=date.today()+timedelta(days=1))
		else:
			move(torm,".trash")
			trash=Trashdb(path=os.path.dirname(os.path.realpath(torm))+"/.trash/"+torm,expiration=date.today()+timedelta(days=1))
		print "Enviado a papelera "+torm
		session.add(trash)
		session.commit()
	else:
		print "No existe "+torm
