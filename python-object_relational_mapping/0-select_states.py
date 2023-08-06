#!/usr/bin/python3
'''script that lists all the data in a table'''
import MySQLdb as mysql
from sys import argv


if __name__=="__main__":
    db = mysql.connect(user=argv[1], passwd=argv[2], db=argv[3], host="localhost", port=3306)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for state in query_rows:
        print(state)
    cur.close()
    conn.close()
