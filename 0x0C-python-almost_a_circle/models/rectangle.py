#!/usr/bin/python3
"""Rectangle subclass"""

Base = __import__('base').Base


class Rectangle(Base):
    """Representation of the Rectangle subclass"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instantiation of the Rectangle class

        Args:
            width(int): The width of the rectangle
            height(int): The height of the rectangle
            x(int): The position of the rectangle on the x axis
            y(int): The position of the rectangle on the y axis

        """
        super(self, Base).__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Function getter to retrieve the width

        Returns:
            int: the current value of the width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Function setter to set the value of the width

        Args:
            value(int): The new value of the width

        """
        self.__width = value

    @property
    def height(self):
        """
        Function getter to retrieve the height

        Returns:
            int: the current value of the height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Function setter to set the value of the height

        Args:
            value(int): The new value of the height

        """
        self.__height = value

    @property
    def x(self):
        """
        Function getter to retrieve the x pos

        Returns:
            int: the current value of x
        """
        return (self.__x)

    @x.setter
    def x(self, value):
        """
        Function setter to set the value of x pos

        Args:
            value(int): The new value of the x

        """
        self.__x = value

    @property
    def y(self):
        """
        Function getter to retrieve the y pos

        Returns:
            int: the current value of y
        """
        return (self.__y)

    @y.setter
    def y(self, value):
        """
        Function setter to set the value of the y pos

        Args:
            value(int): The new value of y

        """
        self.__y = value
