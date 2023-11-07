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

    def area(self):
        """
        Calculates the area of a rectangle object

        Returns:
            float: The area of a rectangle

        """
        return (self.__width * self.__height)

    def __str__(self):
        """stri function to represent a rectangle

         Returns:
            str: a string showing the rectangle dimensions
        """
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
