#!/usr/bin/python3
"""
class Square that defines a square by:

Private instance attribute: size
Instantiation with size (no type/value verification)
You are not allowed to import any module

"""


class Square:
    """
    Class Reprresenting a square with its size

    """
    def __init__(self, size):
        """
        Initialising instance variables
        Args:
            size(int): The size of the square object

        """
        self.__size = size
