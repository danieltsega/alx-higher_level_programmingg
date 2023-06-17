#!/usr/bin/python3

"""
A script to check the table from argument
"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[
        2], host='localhost', port=3306, db=sys.argv[3])
    state_name = sys.argv[4]
    cursor = db.cursor()
    query = 'SELECT * FROM states WHERE name LIKE BINARY "{}" ORDER BY id'
    cursor.execute(query.format(state_name))

    states = cursor.fetchall()
    for row in states:
        print(row)

    cursor.close()
    db.close()
