#!/usr/bin/python3
'''This module uses ORM to query a db'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from relationship_state import State
from relationship_city import Base, City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for s in session.query(State).order_by(State.id).all():
        print(f'{s.id}: {s.name}')
        for c in s.cities:
            print(f'\t{c.id}: {c.name}')
