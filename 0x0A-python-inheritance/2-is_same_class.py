#!/usr/bin/python3
"""This module contains a definition of the function `is_same_class`"""


def is_same_class(obj, a_class):
    """
    Checks wether an object is exactly an instance of the specified
    class or not.

        Args:
            obj(object): the object to be checked
            a_class(object): the class of the instance obj

        Returns:
            bool: True if yes otherwise False

    """
    if type(obj) is a_class:
        return (True)
    return (False)
