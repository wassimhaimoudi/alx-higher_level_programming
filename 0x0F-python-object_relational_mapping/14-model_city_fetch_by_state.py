#!/usr/bin/python3
"""This script displays all City objects from the database
hbtn_0e-6_usa
"""
from sys import argv
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                argv[1], argv[2], argv[3]
                )
            )
    Session = sessionmaker(bind=engine)

    session = Session()

    results = session.query(City, State).join(State)

    for city, state in results.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.commit()
    session.close()
