#!/usr/bin/python3
'''A module defining the class `BaseGeometry`.
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a Rectangle shape
    """
    def __init__(self, width, height):
        """
        Instantiation of the rectangle object

         Args:
            width(int): the width of the rectangle object
            height(int): the height of the rectngle object

        """
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
