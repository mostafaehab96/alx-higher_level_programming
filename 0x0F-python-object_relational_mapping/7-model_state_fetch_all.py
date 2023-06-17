#!/usr/bin/python3
"""Listing all State object in states table
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy import asc
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]),
                           pool_pre_ping=True
                           )
    Base.metadata.create_all(engine)
    session = Session(engine)
    states = session.query(State).order_by(asc(State.id)).all()

    for state in states:
        print(f"{state.id}: {state.name}")
