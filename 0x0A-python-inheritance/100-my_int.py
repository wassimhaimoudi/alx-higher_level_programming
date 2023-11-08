#!/usr/bin/python3
"""This module defines a subclass of the `int `class."""


class MyInt(int):
    def __init__(self, number):
        super().__init__()
        self.__number = number

    def __eq__(self, other):
        """
        Overriding the == operator and inverting its role

        Args:
            other(object): an instance of the int object
        Returns:
            bool: false if there is equality
        """
        if isinstance(other, MyInt):
            return super().__eq__(other)
        return False

    def __ne__(self, other):
        """
        Overriding the != operator and inverting its role

        Args:
            other(int): an instance of the int object
        Returns:
            bool: True if there is no equality
        """
        if isinstance(other, MyInt):
            return super().__ne__(other)
        return True
