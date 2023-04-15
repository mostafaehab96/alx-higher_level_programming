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
        self.__width = value

    @property
    def height(self):
        """Getter for the private height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the private height."""
        self.__height = value

    @property
    def x(self):
        """Getter for the private x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the private x."""
        self.__x = value

    @property
    def y(self):
        """Getter for the private y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the private y."""
        self.__y = value
