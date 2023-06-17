#!/usr/bin/python3
"""
A script to list all cities
"""

import sys
import MySQLdb

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.connect(port=3306, user=user,
                           passwd=password, db=db)
    cursor = conn.cursor()
    cursor.execute("SELECT cities.name FROM cities \
                    JOIN states ON cities.state_id = states.id \
                    WHERE states.name=%s \
                    ORDER BY cities.id ASC", (state_name,))
    cities = cursor.fetchall()
    print(", ".join([row[0] for row in cities]))

    cursor.close()
    conn.close()
