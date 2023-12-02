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

    def to_json(self):
        """
        Retrieves a dictionary representation of the class Student

        Returns:
            dict: A dictionary representation of a Student class
                instance
        """
        return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
                }
