#!/usr/bin/python3
"""
Script to filter states by user input

Usage:
    ./2-my_filter_states.py <username> <password> <database> <state_name>

Connects to a MySQL server running on localhost at port 3306 and
displays all values in the states table where name matches the provided state_name.

Results are sorted in ascending order by states.id.

Arguments:
    - username: MySQL username
    - password: MySQL password
    - database: Database name
    - state_name: State name to be searched

Example:
    ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
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
    query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"
    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
