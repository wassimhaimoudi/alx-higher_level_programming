#!/usr/bin/python3
"""Print State object with the name of the state passed as an argument
from the database hbtn_0e_6_usa
"""
if __name__ == '__main__':
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    my_usr = argv[1]
    my_pwd = argv[2]
    my_db = argv[3]
    my_state = argv[4]

    my_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            my_usr,
            my_pwd,
            my_db
            )
    engine = create_engine(my_url)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State.id).filter(
            State.name.like(my_state)
            ).order_by(State.id).all()

    if result == []:
        print('Not found')
    else:
        for row in result:
            print(row[0])
