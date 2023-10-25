#!/usr/bin/python3
"""
This module has a Class Square that defines a square

"""


class Square:
    """
    Representation of a Square class

    """
    def __init__(self, size=0):
        """Instantiation with size
        Args:
            size(int): The size of the square object

        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
