#!/usr/bin/python3
"""Print all City object from the database hbtn_0e_14_usa
"""

if __name__ == '__main__':
    from sys import argv
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    my_usr = argv[1]
    my_pwd = argv[2]
    my_db = argv[3]

    my_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            my_usr,
            my_pwd,
            my_db
            )

    engine = create_engine(my_url)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(
            State,
            City
            ).join(City, State.id == City.state_id).order_by(City.id)

    for state, city in results.all():
        print('{}: ({}) {}'.format(state.name, city.id, city.name))

    session.commit()
    session.close()
