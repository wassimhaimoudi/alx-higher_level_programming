#!/usr/bin/python3
"""This module defines the function `load_from_json_file`"""
import json


def load_from_json_file(filename):
    """
    Function that creates an Object from a JSON file
    Args:
        filename(str): The absolute or relative path of the JSON file

    Retunrs:
        object: A Python object

    """
    with open(filename, 'r', encoding="utf-8") as f:
        return (json.loads(f.read()))
