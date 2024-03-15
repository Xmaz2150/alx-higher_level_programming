#!/usr/bin/python3
import MySQLdb
from sys import argv

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

    query = "SELECT * FROM {}.states".format(db_name)
    c.execute(query)

    rows = c.fetchall()
    for row in rows:
        print(row)

    c.close()
    db.close()
