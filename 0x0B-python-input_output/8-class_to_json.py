#!/usr/bin/python3
"""This module defines the function `class_to_json`"""


def class_to_json(obj):
    """
    Function that converts a non seriazable class object
    into a into a seriazable data structure for JSON
    representation

    Args:
        obj(object): object to be processed

    Returns:
        dict: a dictionary of attributes
    """
    return (vars(obj))
