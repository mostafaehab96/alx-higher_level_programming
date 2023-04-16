#!/usr/bin/python3

"""Defining a Rectangle class that inherits from Base."""
from models.base import Base


class Rectangle(Base):
    """A simple Rectangle class with width and height."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Intialization of the calss with it's super class
        constructor and width, height, x and y and make it private.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for the private width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the private width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for the private x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the private x."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for the private y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the private y."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Displays the rectangle in form of #."""
        line = "#" * self.__width + '\n'
        print(line * self.__height, end="")

    def __str__(self):
        """Returns the representation of rectangle."""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"\
               f" - {self.__width}/{self.__height}"
