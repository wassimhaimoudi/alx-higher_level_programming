#!/usr/bin/python3


"""
This module defines the `add_integer` function
"""


def add_integer(a, b=98):
    """
    Adds two integers with one taking the default value
    of 98

    Args:
        a(int): first operand
        b(int): second operand

    Returns:
        (int): The sum of a and b
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError('a must be an integer')
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError('b must be an integer')
    a = int(a)
    b = int(b)
    return (a + b)
