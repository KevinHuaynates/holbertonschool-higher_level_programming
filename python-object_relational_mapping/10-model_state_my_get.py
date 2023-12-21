#!/usr/bin/python3
"""
Script to print the State object with the name passed as an argument from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":

    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database), pool_pre_ping=True)
    session = Session(engine)

    try:
        state = session.query(State).filter(State.name == state_name).first()

        if state:
            print(state.id)
        else:
            print("Not found")

    except Exception as e:
        print("Error:", e)

    finally:
        session.close()
