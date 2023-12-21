#!/usr/bin/python3
"""
Script to delete all State objects
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
    Base.metadata.create_all(engine)
    session = Session(engine)

    try:
        states_to_delete = session.query(State).filter(State.name.like('%a%')).all()
        for state in states_to_delete:
            session.delete(state)

        session.commit()

    except Exception as e:
        print("Error:", e)

    finally:
        session.close()

