#!/usr/bin/python3
"""
This module contains the definition of the function `inherits_from`
"""


def inherits_from(obj, a_class):
    """
    Checks if obj is an instance of a_class that inherited
    (directly or indirectly) from a specified class

    Args:
        obj(object): The object to be checked
        a_class(object): The class which the object obj is an
        instance of the subclass of a_class

    Returns:
        bool: True if yes, otherwise False

    """
    return (type(obj) is not a_class and isinstance(obj, a_class))
