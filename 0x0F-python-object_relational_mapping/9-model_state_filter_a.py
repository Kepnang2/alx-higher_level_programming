#!/usr/bin/python3

"""
Module lists all State objects that contain the letter a from the database
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    """
    Not executed when imported
    """

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                           argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State)

    res = query.filter(State.name.ilike("%a%")).order_by(State.id).all()

    for result in res:
        print(f"{result.id}: {result.name}")
