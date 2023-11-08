#!/usr/bin/python3
"""This module defines a subclass `Square`"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representation of a Rectangle shape"""
    def __init__(self, size):
        """
        Instantiation of the Rectangle instance

        Args:
            size(int): the size of the rectangle
        """
        super().__init__(size, size)
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """
        Calculates the area of the Square shape

        Returns:
            float: the value of the area
        """
        return (self.__size ** 2)
