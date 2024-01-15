#!/usr/bin/python3
"""Prints Ths first State object from the database hbtn_0e_6_usa
"""
if __name__ == '__main__':
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    my_usr = argv[1]
    my_pwd = argv[2]
    my_db = argv[3]

    my_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            my_usr,
            my_pwd,
            my_db
            )
    engine = create_engine(my_url)

    Session = sessionmaker(bind=engine)
    session = Session()

    first = session.query(State).order_by(State.id).first()

    if first is not None:
        print('{}: {}'.format(first.id, first.name))
    else:
        print('Nothing')
