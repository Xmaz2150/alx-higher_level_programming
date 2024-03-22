#!/usr/bin/python3
""" Lists all City objects """

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
        query = session.query(City).order_by(City.id).all()
        for city in query:
            print("{}: {} -> {}".format(city.id, city.name, city.state.name))

        session.close()
