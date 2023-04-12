#!/usr/bin/python3

"""Defines a load_from_json_file function."""
import json


def load_from_json_file(filename):
    """Creates python object from json file."""
    with open(filename) as file:
        json_data = file.read()
        py_object = json.loads(json_data)
    return py_object
