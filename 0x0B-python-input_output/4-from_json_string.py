#!/usr/bin/python3
"""This module defines the function `from_json_string` """
import json


def from_json_string(my_str):
    """
    Function that converts a JSON string into a python object

    Args:
        my_str(str): The json strng to be converted

    Returns:
        object: Python data structure object

    """
    return (json.loads(my_str))
