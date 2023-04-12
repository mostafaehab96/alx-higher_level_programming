#!/usr/bin/python3

"""Defines a write_file function."""


def write_file(filename="", txt=""):
    """Writes a txt to filename."""
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(txt)
