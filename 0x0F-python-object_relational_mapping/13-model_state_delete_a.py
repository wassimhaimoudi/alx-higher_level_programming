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

    engine = create_engine(my_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State).filter(
            State.name.like('%a%')).all()

    for row in results:
        session.delete(row)

    session.commit()
    session.close()
