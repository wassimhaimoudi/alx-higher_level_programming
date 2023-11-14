#!/usr/bin/python3
"""This module defines a subclass of `Rectangle` called `Square`"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Representation of a Square shape"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Instantiation of the Rectangle instance

        Args:
            size(int): The size of the square
            x(int): The position of the square around the x axis
            y(int): The position of the square around the y axis
            id(int): The square identifier
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Function getter to retrieve the current value of size

        Returns:
            int: The current value of size
        """
        return (self.width)

    @size.setter
    def size(self, value):
        """
        Function setter to set the old size to value

        Args:
            value(int)
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.width = value
        self.height = value

    def to_dictionary(self):
        """
        Returns a dictionary representation
        of a square

        Returns:
            dict: A dict representation of a square
        """
        return {'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
