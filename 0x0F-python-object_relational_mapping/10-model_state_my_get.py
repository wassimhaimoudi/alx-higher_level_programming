#!/usr/bin/python3
"""This script prints the State object with the name passed
as an argument from the database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    my_usr = argv[1]
    my_pwd = argv[2]
    my_db = argv[3]
    my_state = argv[4]

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.
            format(my_usr, my_pwd, my_db)
            )

    Session = sessionmaker(bind=engine)
    session = Session()

    result_state = session.query(State).filter(
            State.name.like('{}'.format(my_state))
            ).order_by(State.id).first()

    if result_state:
        print(result_state.id)
    else:
        print('Not found')

    session.close()
