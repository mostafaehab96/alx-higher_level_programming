#!/usr/bin/python3
"""Defines a Square class."""


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
