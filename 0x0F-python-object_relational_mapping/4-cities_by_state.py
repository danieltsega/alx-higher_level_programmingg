#!/usr/bin/python3

"""
A script to list all cites
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    conn = MySQLdb.connect(
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )

    cursor = conn.cursor()
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id
    """
    cursor.execute(query)

    states = cursor.fetchall()
    for row in states:
        print(row)

    cursor.close()
    conn.close()
