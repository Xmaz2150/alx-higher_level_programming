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

        db = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=user,
                passwd=passwd,
                db=db_name,
                charset="utf8"
        )

        c = db.cursor()

        select = "SELECT cities.id, cities.name, states.name"
        join = "INNER JOIN states ON cities.state_id = states.id"
        query = "{} FROM cities {}".format(select, join)

        c.execute(query)
        rows = c.fetchall()
        for row in rows:
            print(row)

        c.close()
        db.close()
