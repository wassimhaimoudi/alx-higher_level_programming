#!/usr/bin/python3
"""This module defines the `Student` class"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """
        Instantiation of the Student object

        Args:
            (str): The first name of the student
            (str): The last name of the student
            (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the class Student

        Returns:
            dict: A dictionary representation of a Student class
                instance
        """
        if isinstance(attrs, list) and all(type(a) is str for a in attrs):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        else:
            return self.__dict__
