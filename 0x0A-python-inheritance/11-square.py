#!/usr/bin/python3
"""Defines a Square class."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Simple square class."""

    def __init__(self, size):
        """Intialize square with size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculated the area of square."""
        return self.__size ** 2

    def __str__(self):
        """Return description of the square."""
        return f"[Square] {self.__size}/{self.__size}"
