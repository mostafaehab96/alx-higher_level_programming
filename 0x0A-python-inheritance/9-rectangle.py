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

    def area(self):
        """Calculates the area of rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns the description of rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"
