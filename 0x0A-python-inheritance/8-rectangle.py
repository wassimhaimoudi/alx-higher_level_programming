#!/usr/bin/python3
'''A module defining the class `BaseGeometry`.
'''


class BaseGeometry:
    '''The base class for all geometry objects.
    '''
    def area(self):
        '''Computes the area of this geometry.

        Returns:
            float: The area of this geometry object.
        '''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Validates an object expected to be a positive and
        non-zero integer object.

        Args:
            name (str): The name of the integer value.
            value (int): The object to validate.
        '''
        if type(value) is not int:
            raise TypeError('{:s} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{:s} must be greater than 0'.format(name))


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
