#!/usr/bin/python3
"""
Script to list all cities of a specific state from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:]
    db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()
    query = """
            SELECT GROUP_CONCAT(name ORDER BY cities.id ASC SEPARATOR ', ')
            """
    cursor.execute(query, (state_name,))

    result = cursor.fetchone()[0]

    print(result)

    cursor.close()
    db.close()

