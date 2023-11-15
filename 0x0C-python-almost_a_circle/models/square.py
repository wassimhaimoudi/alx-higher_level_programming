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

    def update(self, *args, **kwargs):
        """
        updates the Square subclass by assigning to the class instance
        attributes:
        1. 1st argument should be the id attribute
        2. 2nd argument should be the size attribute
        3. 3rd argument should be the x attribute
        4. 4th argument should be the y attribute
        """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) is not int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) is not int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
