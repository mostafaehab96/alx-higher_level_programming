#!/usr/bin/python3

"""Defines to_json_string function."""
import json


def to_json_string(my_obj):
    """Converts s python object to json string."""
    return json.dumps(my_obj)
