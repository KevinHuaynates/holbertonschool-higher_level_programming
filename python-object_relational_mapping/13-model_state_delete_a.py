#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter a
"""

import sys
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    try:
        delete_query = text("DELETE FROM states WHERE name LIKE :pattern")
        session.execute(delete_query, {"pattern": "%a%"})

        session.commit()

    except Exception as e:
        print("Error:", e)
        session.rollback()

    finally:
        session.close()
