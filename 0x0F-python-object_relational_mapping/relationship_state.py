#!/usr/bin/python3
'''This module defines an ORM'''

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import relationship
from relationship_city import Base


class State(Base):
    '''This represents the states table'''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    cities = relationship('City', backref='state', cascade='delete')


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format('root', 'root', 'hbtn_0e_100_usa'),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
