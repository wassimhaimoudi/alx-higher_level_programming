#!/usr/bin/python3
"""This module contains the definition of the function `lookup`"""


def lookup(obj):
    """
    Returns a list of attributes and methods of an object
        Args:
            obj(object): The input object to be processed.

        Returns:
            list: A list object of attributes and methods.

    """
    return (dir(obj))
