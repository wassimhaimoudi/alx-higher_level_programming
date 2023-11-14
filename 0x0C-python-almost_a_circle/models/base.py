#!/usr/bin/python3
"""This module defines a base class called `Base`"""
import json


class Base:
    """Representation of the `Base` class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Instantiation of the Base class

        Args:
            id(int): Identifier of objects

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns aa JSON representation of a list of dicts

        Args:
            list_dictionaries(list): The list to be JSON
            represented

        Returns:
            str: A JSON string representation
        """
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes a JSON representation of a list of objects
        to a json file

        Args:
            list_objs(list): The list of objects to be stored in
            a json file
        """
        obj_json = to_json_string(list_objs)
        with open('{}.json'.format(cls.__name__), 'w'):
            f.write(obj_json)
