#!/usr/bin/python3
"""Contains City class definition
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """Represents a city object

    Attributes:
        __tablename__ (str): Represents the table name.
        id (int): Reresents the column of the city id.
        name (str): Represents a column of the city name.
        state_id (str): Represents a column of the state object id.
    """

    __tablename__ = 'cities'
    id = Column(
            Integer,
            primary_key=True,
            unique=True,
            autoincrement=True,
            nullable=False
            )
    name = Column(String(128), nullable=False)
    state_id = Column(
            String(128),
            ForeignKey('state.id'),
            nullable=True
            )
