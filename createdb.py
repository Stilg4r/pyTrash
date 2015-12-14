#!/usr/bin/env python

import os
import sys
from sqlalchemy import Column, Integer, String, Date  
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

import config
 
Base = declarative_base()
 
class Trashdb(Base):
    __tablename__ = 'trashdb'
    id = Column(Integer, primary_key = True)
    path = Column(String)#, nullable = False
    expiration = Column(Date)#, nullable = False

engine = create_engine(config.db)

Base.metadata.create_all(engine)
