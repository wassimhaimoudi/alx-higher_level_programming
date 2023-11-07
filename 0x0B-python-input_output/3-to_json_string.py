#!/usr/bin/python3
"""This module defines the function `to_json_string`"""
import json


def to_json_string(my_obj):
    """
    JSON representation of an object

    Args:
        my_obj(object): The object to be JSON represented

    Returns:
        str: a json string representation of the object

    """
    return (json.dumps(my_obj))
