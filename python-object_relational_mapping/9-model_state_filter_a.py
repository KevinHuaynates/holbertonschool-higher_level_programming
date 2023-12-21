#!/usr/bin/python3
"""
Script to list all State objects containing the letter 'a' from the database hbtn_0e_6_usa
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
        states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()
        for state in states_with_a:
            print("{}: {}".format(state.id, state.name))

    except Exception as e:
        print("Error:", e)

    finally:
        session.close()
