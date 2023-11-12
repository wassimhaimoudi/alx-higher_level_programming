#!/usr/bin/python3
"""This module defines a base class called `Base`"""


class Base:
    """Representation of the `Base` class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Instantiation of the Base class

        Args:
            id(int): Identifier of objects

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
