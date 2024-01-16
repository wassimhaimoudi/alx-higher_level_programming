#!/usr/bin/python3
"""Adds State object `Louisiana` to the database hbtn_0e_6_usa
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
    
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name='Louisiana')
    session.add(new_state)
    new_instance = session.query(State).filter_by(
            name='Louisiana').first()
    print(new_instance.id)
    session.commit()
