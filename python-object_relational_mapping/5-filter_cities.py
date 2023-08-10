#!/usr/bin/python3
"""Script to retrieve data from a database"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],
                         host='localhost', port=3306)
    cur = db.cursor()
    cur.execute("SELECT c.name \
                 FROM cities c INNER JOIN states s \
                 ON c.state_id = s.id WHERE s.name = %s\
                 ORDER BY c.id", (sys.argv[4], ))
    query_rows = cur.fetchall()

    for i in range(len(query_rows)):
        print(query_rows[i][0], end=", " if i + 1 < len(query_rows) else "")
    print("")

    cur.close()
    db.close()
