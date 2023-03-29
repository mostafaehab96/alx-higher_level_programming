#!/usr/bin/python3

"""This module define a simple class Square."""


class Square:
    """A simple class Square.
    Attributes:
        size (int): the size of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """The init method initializes the size of the square."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter for private position."""
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is tuple:
            if len(list(filter(lambda x: type(x) is int and x >= 0, value)))\
                    == 2:
                self.__position = value
                return
        raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """prints the square on the screen using # with postion of (x, y)."""
        if self.__size > 0:
            print("\n" * self.__position[1], end="")
            line = " " * self.__position[0] + "#" * self.__size + "\n"
            print(line * self.__size, end="")
        else:
            print()

    def __repr__(self):
        """returns the string representing the square."""
        if self.__size > 0:
            y = "\n" * self.__position[1]
            line = " " * self.__position[0] + "#" * self.__size + "\n"
            return y + (line * self.__size)[0: -1]
        else:
            return ""
