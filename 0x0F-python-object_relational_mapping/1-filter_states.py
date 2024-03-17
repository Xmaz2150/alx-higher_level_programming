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

        query = "SELECT * FROM {}.states ORDER BY id ASC".format(db_name)
        c.execute(query)

        rows = c.fetchall()
        for row in rows:
            if row[1][0] == 'N':
                print(row)

        c.close()
        db.close()
