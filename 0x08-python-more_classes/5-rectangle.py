#!/usr/bin/python3

"""This module defines a simple Rectangle class."""


class Rectangle:
    """A Rectangle class.
    width: int > 0
    height: int > 0
    """
    def __init__(self, width=0, height=0):
        """Initialize rectangle with width and height
        and default value of zero.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for private width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for private width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Getter for the private height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the private height."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Calculates the area of rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculated the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """For printing the rectangle in the form of #."""
        if self.__width == 0 or self.__height == 0:
            return ""
        lines = ["#" * self.__width for i in range(self.__height)]
        lines = "\n".join(lines)
        return lines

    def __repr__(self):
        """For creating the instance with string using eval."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """For deleting an instance."""
        print("Bye rectangle...")
