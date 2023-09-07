from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine


engine = create_engine('sqlite:///codecollab.db')

Session = sessionmaker(engine)
session = Session()

Base = declarative_base()
Base.metadata.create_all(engine)