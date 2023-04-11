#!/usr/bin/python3

"""Defines a class MyList the inherits list."""


class MyList(list):
    """Class inherits form list
    and have a print_sorted method.
    """

    def print_sorted(self):
        """Prints a sorted list."""
        print(sorted(self))
