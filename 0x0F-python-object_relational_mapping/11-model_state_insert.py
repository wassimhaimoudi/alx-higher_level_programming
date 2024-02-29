#!/usr/bin/python3
"""This script add the State 'Louisiana' to the database hbtn_0e_6_usa
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

    new_state = State(id=6, name='Louisiana')
    session.add(new_state)
    session.commit()

    result_state = session.query(State).filter(
            State.name.like('{}'.format(new_state.name))
            ).first()

    print(result_state.id)
    session.close()
