#!/usr/bin/python3
"""
This file contains class definition of a State
and an instance of Base = declarative_base()
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    Represents State Class

    Attributes:
        __tablename__ (str): the name of the table this class is mapped to
        id (int): A column from the table representing the state identifier
        name (str): A column from the table representing the state name
    """

    __tablename__ = 'states'
    id = Column(
            Integer,
            primary_key=True,
            unique=True,
            autoincrement=True,
            nullable=False
        )
    name = Column(String(128), nullable=False)
