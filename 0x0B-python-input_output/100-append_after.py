#!/usr/bin/python3

"""Defines append_after function."""


def append_after(filename="", search_string="", new_string=""):
    """Appends new_string after each line containing search_string."""

    with open(filename, "r") as file:
        lines = file.readlines()
        new_lines = lines[:]
        i = 0
        for line in lines:
            if line.find(search_string) != -1:
                new_lines.insert(i + 1, new_string)
                i += 1
            i += 1
    with open(filename, "w") as file:
        file.writelines(new_lines)
