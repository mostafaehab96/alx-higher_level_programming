#!/usr/bin/python3
"""Defines has attribute function."""


def add_attribute(obj, name, value):
    """Adds attribute if possible."""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
