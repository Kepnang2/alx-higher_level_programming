#!/usr/bin/python3
"""
model_city.py that contains the class definition of a City
"""

from model_state import Base, State
from sqlalchemy import Integer, String, Column, ForeignKey


class City(Base):
    """
    class definition of a City
    """
    __tablename__ = "cities"

    id = Column(Integer, autoincrement=True, unique=True, nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
