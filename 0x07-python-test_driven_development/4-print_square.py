#!/usr/bin/python3

"""Defines a simple print_square function."""


def print_square(size):
    """Prints a square with size 'size' in form of #."""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    lines = ["#" * size for i in range(size)]
    lines = "\n".join(lines)
    print(lines)
