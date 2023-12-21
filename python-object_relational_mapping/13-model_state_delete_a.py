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
        result = session.query(State.name, City.id, City.name).join(City).order_by(City.id).all()
        for state_name, city_id, city_name in result:
            print("{}: ({}) {}".format(state_name, city_id, city_name))

    except Exception as e:
        print("Error:", e)

    finally:
        session.close()

