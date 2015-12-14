#!/usr/bin/env python

from sqlalchemy import create_engine
from createdb import Base, Trashdb
from sqlalchemy.orm import sessionmaker
from os import remove 

import config

engine = create_engine(config.db)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

for file2delete in session.query(Trashdb).filter_by(expiration=date.today()):
    remove(file2delete.path)
    session.delete(t)
session.commit()
