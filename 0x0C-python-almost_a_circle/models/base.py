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

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation

        Args:
            json_string(str): JSON string representation

        Returns:
            list: A list of the JSON string representation
        """
        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes a JSON representation of a list of objects
        to a json file

        Args:
            list_objs(list): The list of objects to be stored in
            a json file
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance of the class `cls` with all
        attributes already set.

        Args:
            dictionary(dict): A dict representation of a class instance

        Returns:
            obj: A python class instance or object.
        """
        dummy = cls(4, 3, 2)
        dummy.update(**dictionary)
        return (dummy)
