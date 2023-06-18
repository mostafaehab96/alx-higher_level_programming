#!/usr/bin/python3
"""Add new  State object with a specified name
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy import asc
from sqlalchemy.orm import Session
from sqlalchemy import select

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]),
                           pool_pre_ping=True
                           )
    state = State(name="Louisiana")
    Base.metadata.create_all(engine)
    session = Session(engine)
    session.add(state)
    session.commit()

    print(state.id)
