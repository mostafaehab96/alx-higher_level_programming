#!/usr/bin/python3

"""Defines class BaseGeomtry."""


class BaseGeometry:
    """BaseGeometry class empty."""

    def area(self):
        """Basic area function."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value is integer."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be greater than 0")
