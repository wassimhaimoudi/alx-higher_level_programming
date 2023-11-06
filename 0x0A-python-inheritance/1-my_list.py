#!/usr/bin/python3
"""This module contains the definition of a class"""


class MyList(list):
    """Represents a list"""
    def __init__(self):
        """
        Instantiation of the MyList instance
        Invokation of the parent class
        """
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
