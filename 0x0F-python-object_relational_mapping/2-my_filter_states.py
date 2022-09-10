#!/usr/bin/python3
'''
This script lists data in a database
It takes an argument for searching
'''

import sys
import MySQLdb

if __name__ == '__main__':
    u = sys.argv[1]
    p = sys.argv[2]
    d = sys.argv[3]
    conn = MySQLdb.connect(host="localhost", port=3306, user=u, passwd=p,
                           db=d, charset="utf8")
    cur = conn.cursor()
    n = sys.argv[4]
    cur.execute("SELECT id, name FROM states WHERE name='{:s}' ORDER BY id ASC"
                .format(n))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
