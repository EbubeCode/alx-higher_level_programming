#!/usr/bin/python3
'''This module uses ORM to query a db'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = {}
    for c in session.query(City).order_by(City.id).all():
        s = ''
        id = c.state_id
        if states.get(id):
            s = states[id]
        else:
            state = session.query(State).filter(State.id == id).first()
            s = state.name
        print(f'{s}: ({c.id}) {c.name}')
