#!/usr/bin/python3
"""This module contains a class called `Square`"""


class Square:
    """Represents a square shape"""
    def __init__(self, size=0, position=(0, 0)):
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

        if type(position) is not tuple or
            any(type(num) is not int for num in position) or
            len(value) != 2 or any(num >= 0 for num in value):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = position

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

    @property
    def position(self):
        """
        Function getter to retrieve the value of the position

        Returns:
            (tuple): A tuple of 2 positive integers

        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        Function setter to change the value of the position

        Args:
            value(tuple): The position of the square object

        """
        if type(value) is not tuple or len(value) != 2 or
            any(type(num) for num in value) or
            any(num >= 0 for num in value)):
        self.__position = value

     def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
