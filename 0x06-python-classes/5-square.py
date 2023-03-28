#!/usr/bin/python3

"""This module define a simple class Square."""


class Square:
    """A simple class Square.
    Attributes:
        size (int): the size of the square
    """
    def __init__(self, size=0):
        """The init method initializes the size of the square."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size

    def area(self):
        """Calculate the area of the square.
        Returns:
            int: the area
        """
        return self.__size ** 2

    @property
    def size(self):
        """Getter for private size."""
        return self.__size

    @size.setter
    def size(self, size):
        """Setter for private size."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def my_print(self):
        """prints the square on the screen using #."""
        line = "#" * self.__size + "\n"
        print(line * self.__size, end="" if self.__size > 0 else "\n")
