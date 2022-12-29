#!/usr/bin/python3

"""
prints the State object with the name passed as argument from the database
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    """
    prints the State object with the name passed as argument from the database
    """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                           argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).filter(State.name == argv[4]).first()

    if (result):
        print(result.id)
    else:
        print("Not found")
