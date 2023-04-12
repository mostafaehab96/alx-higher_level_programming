#!/usr/bin/python3

"""Defines a read_file function."""


def read_file(filename=""):
    """Reads filename and print it to stdout."""
    with open(filename, mode="r", encoding="utf-8") as file:
        print(file.read(), end="")
