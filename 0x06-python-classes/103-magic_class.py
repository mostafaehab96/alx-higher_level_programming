#!/usr/bin/python3

"""Defining a magic class from bytecode which looks like a circle class"""
import math


class MagicClass:
    """The magic class to define
    radius: int or float
    """
    def __init__(self, radius=0):
        """Initialization with radius."""
        if type(radius) is not int:
            if type(radius) is not float:
                raise TypeError("radius must be a number")
        else:
            self.radius = radius

    def area(self):
        """Calculating area of a circle."""
        return math.pi * (self.radius ** 2)

    def circumference(self):
        """Calculating circumferecne of a circle."""
        return 2 * math.pi * self.radius
