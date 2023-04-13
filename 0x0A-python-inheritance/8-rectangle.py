#!/usr/bin/python3
"""Defines a class Rectangle that inherits BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Simple Rectangle class."""

    def __init__(self, width, height):
        """intialized with width and height must be int."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
