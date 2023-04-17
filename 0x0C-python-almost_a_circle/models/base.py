#!/usr/bin/python3

"""Defining simple Base class."""
import json


class Base:
    """A simple Base class."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize class with id."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries."""
        if (list_dictionaries is None
                or len(list_dictionaries) == 0):
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        data = []
        for obj in list_objs:
            data.append(obj.to_dictionary())
        data = Base.to_json_string(data)
        filename = f"{cls.__name__}.json"
        with open(filename, "w") as file:
            file.write(data)
