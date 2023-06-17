#!/usr/bin/python3

"""
Filter and list a data from the table
"""

import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[
        1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states \
            WHERE name LIKE BINARY 'N%' \
            ORDER BY states.id")

    state = cursor.fetchall()
    for row in state:
        print(row)

    cursor.close()
    conn.close()
