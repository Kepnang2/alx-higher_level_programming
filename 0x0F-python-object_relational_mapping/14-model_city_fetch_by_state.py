#!/usr/bin/python3

"""
model_city.py that contains the class definition of a City
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    """
    Not to be executed when imported
    """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                           argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(City, State)
    res = query.join(State, State.id == City.state_id).order_by(City.id).all()

    for city, state in res:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
