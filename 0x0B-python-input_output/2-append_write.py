#!/usr/bin/python3

"""Defines appen_file function."""


def append_write(filename="", text=""):
    """Appends text to filename."""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
