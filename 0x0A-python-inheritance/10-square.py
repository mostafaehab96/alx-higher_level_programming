#!/usr/bin/python3
"""Defines a Square class."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Simple square class."""

    def __init__(self, size):
        """Intialize square with size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculated the area of square."""
        return self.__size ** 2
