#!/usr/bin/python3

"""
deletes all State objects with a name containing the letter a from the database
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    """
    Not to be executed
    """

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                           argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State).filter(State.name.ilike("%a%")).all()

    for result in results:
        session.delete(result)

    session.commit()
