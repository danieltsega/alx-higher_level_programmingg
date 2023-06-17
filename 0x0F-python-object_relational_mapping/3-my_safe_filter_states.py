#!/usr/bin/python3

"""
A script to safley search
"""

import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[
        2], host='localhost', port=3306, db=sys.argv[3])
    state_name = sys.argv[4]
    cursor = conn.cursor()
    q = 'SELECT * FROM states WHERE name = %s ORDER BY id'
    cursor.execute(q, (state_name,))

    states = cursor.fetchall()
    for row in states:
        print(row)

    cursor.close()
    conn.close()
