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

    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries."""
        if (list_dictionaries is None
                or len(list_dictionaries) == 0):
            return "[]"

        return json.dumps(list_dictionaries)
