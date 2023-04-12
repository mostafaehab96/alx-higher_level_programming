#!/usr/bin/python3

"""Defines class to object function."""


def class_to_json(obj):
    """Return a python dict from class attributes."""
    attributes = [attr for attr in dir(obj) if not callable
                  (getattr(obj, attr)) and not attr.startswith("__")]
    attribute_dict = {attr: getattr(obj, attr) for attr in attributes}
    return attribute_dict
