#!/usr/bin/python3
"""This module contains a class called `Square`"""


class Square:
    """Represents a square shape"""
    def __init__(self, size=0):
        """
        Instantiation with optional size
        Args:
            size(int): The size of the square object

        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size mustbe >= 0')
        self.__size = size

    def area(self):
        """
        Function that calculates the area of a square

        Returns:
            int: the area of the square object

        """
        return ((self.__size)**2)
