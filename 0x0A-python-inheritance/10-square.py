#!/usr/bin/python3
"""Defines a Square class."""

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
