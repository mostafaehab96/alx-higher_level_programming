#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """A simple class student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a class."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dict representation of class."""
        if (attrs and type(attrs) is list and
                all([type(i) is str for i in attrs])):
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json):
        """Update class attributes."""
        for key, value in json.items():
            setattr(self, key, value)
