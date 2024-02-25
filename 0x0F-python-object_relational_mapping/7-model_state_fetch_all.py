#!/usr/bin/python3
"""This script lists all State objects from the database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    my_usr = argv[1]
    my_pwd = argv[2]
    my_db = argv[3]

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.
            format(my_usr, my_pwd, my_db)
            )

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id).all():
        print('{}: {}'.format(state.id, state.name))
