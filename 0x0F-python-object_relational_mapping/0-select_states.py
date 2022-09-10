#!/usr/bin/python3
'''This script lists data in a database'''

import sys
import MySQLdb

if __name__ == '__main__':
    if len(sys.argv) != 4:
        exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=username, passwd=password,
                           db=db, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
