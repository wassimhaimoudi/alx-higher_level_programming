#!/usr/bin/python3
"""File contains class definition of a State and an instance of
Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()


class State(Base):
    """Represents a state instance
    """
    __tablename__ = 'states'
    id = Column(
            Integer,
            primary_key=True,
            nullable=False,
            unique=True
            )
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")
