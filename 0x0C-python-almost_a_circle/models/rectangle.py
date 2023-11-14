#!/usr/bin/python3
"""Rectangle subclass"""

from models.base import Base


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

        Raises:
            TypeError: If neither the width nor the height are ints
            ValueError: If neither the width or the height > 0
            TypeError: If neither the x nor y are ints
            ValueError: If neither x or y >= 0

        """
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if type(y) is not int:
            raise TypeError('y must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        if height <= 0:
            raise ValueError('height must be > 0')
        if x < 0:
            raise ValueError('x must be >= 0')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

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
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
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
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
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
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise TypeError('x must be >= 0')
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
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise TypeError('y must be >= 0')
        self.__y = value

    def area(self):
        """
        Calculates the Rectangle area

        Returns:
            float: The value of the rectangle area
        """
        return (self.__width * self.__height)

    def display(self):
        """
        Displays a rectangle representation
        using the character `#`

        Returns:
            None
        """
        for y1 in range(1, self.__y + 1):
            print()
        for i in range(self.__height):
            for x1 in range(1, self.__x + 1):
                print(' ', end='')
            for j in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        """
        Return a string representation of the object.

        This method is called by the built-in str() function and the print()
        function to obtain a string representation of the object.

        Returns:
            str: A string representation of the object
        """
        s = '[Rectangle] ({}) {}/{} - {}/{}'
        return s.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
        Updates instance attributes by assigning to each of them:

        1. 1st argument should be the id attribute
        2. 2nd argument should be the width attribute
        3. 3rd argument should be the height attribute
        4. 4th argument should be the x attribute
        5. 5th argument should be the y attribute

        Args:
            args(list): a list of positional arguments
            kwargs(dict): a dict of keyword arguments

        """
        if args:
            if len(args) == 0:
                return
            if len(args) > 0:
                self.__id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]

    def to_dictionary(self):
        """
        Returns a dictionary representatio
        of a Rectangle

        Returns:
            dict: A dictionary representation
            of a Rectangle
        """
        return {'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y}
