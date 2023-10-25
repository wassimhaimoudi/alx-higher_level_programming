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
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """
        Function that calculates the area of a square

        Returns:
            int: the area of the square object

        """
        return ((self.__size)**2)

    @property
    def size(self):
        """
        Function getter to retieve the size attribute

        Returns:
            int: The size of the square object

        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Function setter to set the value of the size
        of the square object optionally

        Args:
            value(int): The value of the new sizeof the square object

        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        """Function That prints out a square using the character `#`"""
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
