#!/usr/bin/python3
"""Script to retrieve data from a database"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect("localhost", user=sys.argv[1], port=3306,
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
                JOIN states ON cities.state_id = states.id \
                ORDER BY cities.id")

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    db.close()
