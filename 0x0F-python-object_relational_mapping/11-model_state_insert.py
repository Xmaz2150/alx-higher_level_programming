#!/usr/bin/python3

"""
    lists states in database
"""

from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from sys import argv
from model_state import Base, State

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
        new_state = State(name="Louisiana")
        session.add(new_state)
        session.commit()

        print(new_state.id)
        session.close()
