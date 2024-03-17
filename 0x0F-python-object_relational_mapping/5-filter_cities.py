#!/usr/bin/python3

"""
    lists states in database
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    ac = len(argv)

    if ac < 4:
        exit(1)
    else:
        user = argv[1]
        passwd = argv[2]
        db_name = argv[3]
        state = argv[4]

        db = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=user,
                passwd=passwd,
                db=db_name,
                charset="utf8"
        )

        c = db.cursor()

        select = "cities.id, cities.name, states.name"

        state_name = "WHERE states.name='{}'".format(state)
        join = "states ON cities.state_id = states.id {}".format(state_name)

        query = "SELECT {} FROM cities INNER JOIN {}".format(select, join)

        c.execute(query)
        rows = c.fetchall()

        cities = []
        for row in rows:
            cities.append(row[1])
        print(', '.join(cities))

        c.close()
        db.close()
