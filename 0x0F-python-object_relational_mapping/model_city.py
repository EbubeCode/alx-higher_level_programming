#!/usr/bin/python3
'''This module defines an ORM'''

from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    '''This represents the cities table'''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey('states.id'))


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format('root', 'root', 'hbtn_0e_14_usa'),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
