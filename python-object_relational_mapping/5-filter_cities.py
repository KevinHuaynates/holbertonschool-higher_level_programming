#!/usr/bin/python3
"""Script to list all cities of a specific state from the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:]

    db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)

    cursor = db.cursor()

    try:
        query = "SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = %s) ORDER BY id ASC"
        cursor.execute(query, (state_name,))

        rows = cursor.fetchall()
        result = ', '.join([row[1] for row in rows])
        print(result)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        cursor.close()
        db.close()
