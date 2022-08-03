# -*- coding: UTF-8 -*-
# from sqlalchemy.ext.declarative import as_declarative
#  from sqlalchemy import create_engine, inspect
#  from sqlalchemy.orm import sessionmaker
from sqlmodel import create_engine
import os

dbUser = os.environ.get('POSTGRES_USER')
dbPassword = os.environ.get('POSTGRES_PASSWORD')
dbServer = os.environ.get('POSTGRES_SERVER')
dbPort = os.environ.get('POSTGRES_PORT')
dbName = os.environ.get('POSTGRES_DB')

print(os.environ.get('DATABASE_URL'))
dburl = os.environ.get('DATABASE_URL')

# create an engine
engine = create_engine(dburl, echo=True)

