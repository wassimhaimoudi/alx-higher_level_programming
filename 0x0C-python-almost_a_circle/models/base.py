#!/usr/bin/python3
"""This module defines a base class called `Base`"""
import json
import os
import csv
import turtle


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
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(3, 2)
            else:
                dummy = cls(3)
            dummy.update(**dictionary)
            return (dummy)

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + '.json'
        try:
            with open(filename, 'r') as f:
                json_list = cls.from_json_string(f.read())
        except FileNotFoundError:
            return []
        instances_list = []
        for o_dict in json_list:
            instances_list.append(cls.create(**o_dict))
        return (instances_list)

    @classmethod
    def load_from_file_cvs(cls):
        """
        deserializes in CSV

        Returns:
            obj: A python object
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_cvs(cls):
        """
        Seriises in CSV
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
