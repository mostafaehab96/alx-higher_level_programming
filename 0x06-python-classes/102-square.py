#!/usr/bin/python3

"""This module define a simple class Square."""


class Square:
    """A simple class Square.
    Attributes:
        size (int): the size of the square
    """
    def __init__(self, size=0):
        """The init method initializes the size of the square."""
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

    def __eq__(self, other):
        """square1 is equal to square2"""
        return self.area() == other.area()

    def __ne__(self, other):
        """square1 is not equal to square2"""
        return self.area() != other.area()

    def __ge__(self, other):
        """square1 is greater then or equal to square2"""
        return self.area() >= other.area()

    def __le__(self, other):
        """square1 is less than or equal to square2"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """square1 is greater than square2"""
        return self.area() > other.area()

    def __lt__(self, other):
        """square1 is less than square2"""
        return self.area() < other.area()
