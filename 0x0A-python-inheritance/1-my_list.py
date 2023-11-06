#!/usr/bin/python3
"""This module contains the definition of a class"""


class MyList(list):
    """Represents a subclass of  list"""

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
