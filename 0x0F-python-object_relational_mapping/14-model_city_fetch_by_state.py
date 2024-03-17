#!/usr/bin/python3

"""
    lists states in database
"""

from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from sys import argv
from model_state import Base, State
from model_city import City

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
        query = session.query(City, State)
        filter_q = query.filter(City.state_id == State.id)
        rows = filter_q.order_by(City.id.asc()).all()

        for cities, states in rows:
            print("{}: ({}) {}".format(states.name, cities.id, cities.name))

        session.close()
