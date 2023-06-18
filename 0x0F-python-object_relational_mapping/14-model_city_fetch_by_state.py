#!/usr/bin/python3
"""Lists all cities and states
"""
import sys
from model_state import Base, State
from model_city import City

from sqlalchemy import (create_engine)
from sqlalchemy import asc
from sqlalchemy.orm import Session
from sqlalchemy import select, join

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]),
                           pool_pre_ping=True
                           )
    Base.metadata.create_all(engine)
    session = Session(engine)
    query = (select(City.id, City.name, State.name)
             .join(State, City.state_id == State.id))
    results = session.execute(query).fetchall()

    for result in results:
        city_id, city_name, state_name = result
        print(f"{state_name}: ({city_id}) {city_name}")
