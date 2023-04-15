#!/usr/bin/python3

"""Defining simple Base class."""


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
