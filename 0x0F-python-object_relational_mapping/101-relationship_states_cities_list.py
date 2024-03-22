#!/usr/bin/python3
""" Lists all State objects and corresponding City objects """

from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from sys import argv
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    ac = len(argv)

    if ac < 4:
        exit(1)
    else:
        user = argv[1]
        passwd = argv[2]
        db_name = argv[3]

        engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost/{}'.format
                (user, passwd, db_name),
                pool_pre_ping=True
        )

        Base.metadata.create_all(engine)

        session = Session(engine)
        query = session.query(State).order_by(State.id).all()
        for state in query:
            print("{}: {}".format(state.id, state.name))
            for city in state.cities:
                print("\t{}: {}".format(city.id, city.name))

        session.close()