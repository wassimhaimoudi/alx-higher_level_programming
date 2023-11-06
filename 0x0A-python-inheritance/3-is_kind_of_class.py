#!/usr/bin/python3
"""
This mole contains the definition of the function `is_kind_of_class`
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if obj is instance of a_class or if obj is an instance of
    a class that inherited from a_class

        Args:
            obj(object): The object to be checked
            a_class(object): the class that obj should be
                            an instance of.

        Returns:
        bool: True if yes, otherwise False

    """
    return (isinstance(obj, a_class) or issubclass(type(obj), a_class))
