#!/usr/bin/python3

"""Modulo: Script to filter states by user input"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check if all required arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Get command line arguments
    username, password, database, state_name = sys.argv[1:]
    
    # Connect to MySQL server
    db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Prepare and execute SQL query
    query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Fetch all the rows
    rows = cursor.fetchall()
    
    # Display the results
    for row in rows:
        print(row)

    # Close cursor and connection
    cursor.close()
    db.close()
