#!/usr/bin/python3
'''This script lists data in a database'''

import sys
import MySQLdb

if __name__ == '__main__':
    if len(sys.argv) < 5:
        exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=username, passwd=password,
                           db=db, charset="utf8")
    cur = conn.cursor()
    name = sys.argv[4]
    query = 'SELECT c.name FROM cities c JOIN '
    query += 'states s ON state_id = s.id WHERE s.name = %s'
    query += ' ORDER BY c.id ASC'
    cur.execute(query, (name,))
    query_rows = cur.fetchall()
    cities = ''
    for row in query_rows:
        if cities != '':
            cities += ', '
        cities += row[0]
    print(cities)
    cur.close()
    conn.close()
