#!/usr/bin/python3
"""This model defines the class `BaseGeomtry`"""


class BaseGeometry:
    """Represents a BaseGeometry class"""
    def area(self):
        """
        Calculates the area of something
        """
        raise Exception("area() is not implemented")
