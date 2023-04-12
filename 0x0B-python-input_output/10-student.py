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
            class_dict = {}
            for attr in attrs:
                try:
                    class_dict[attr] = getattr(self, attr)
                except AttributeError:
                    pass
            return class_dict
        return {"first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
                }
