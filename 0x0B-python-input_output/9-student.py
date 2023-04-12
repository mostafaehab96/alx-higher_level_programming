#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """A simple class student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a class."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dict representation of class."""
        return {"first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
                }
