#!/usr/bin/python3

"""
 lists all State objects from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == '__main__':
    """
    Not executed when imported
    """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                           argv[2], argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State).order_by(State.id).all()

    for result in results:
        print("{}: {}".format(result.id, result.name))
