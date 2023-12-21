#!/usr/bin/python3
"""
Script to print the first State object from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database), pool_pre_ping=True)
    session = Session(engine)

    try:
        first_state = session.query(State).order_by(State.id).first()
        if first_state is not None:
            print("{}: {}".format(first_state.id, first_state.name))

        else:
            print("Nothing")

    except Exception as e:
        print("Error:", e)

    finally:
        session.close()
