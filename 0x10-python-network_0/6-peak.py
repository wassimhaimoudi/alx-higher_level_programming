#!/usr/bin/python3
"""This module defines a function called `find_peak`
that finds a peak in a list of unsorted integers
"""


def find_peak(my_list: list):
    """ finds peak in a list of unsorted integers
        Args:
            my_list[list]: The list to search in.
        Returns:
            (int): The peak element in my_list
    """
    if not my_list:
        return None
    if len(my_list) == 1:
        return my_list[0]

    a, b = 0, len(my_list) - 1

    while a <= b:
        mid = (a + b) // 2
        if (mid == 0 or my_list[mid] >= my_list[mid - 1]) and
        (mid == len(my_list) - 1 or my_list[mid] >= my_list[mid + 1]):
            return my_list[mid]
        elif mid < len(my_list) - 1 and my_list[mid] < my_list[mid + 1]:
            a = mid + 1
        else:
            b = mid - 1
