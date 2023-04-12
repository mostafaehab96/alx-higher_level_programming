#!/usr/bin/python3

"""Defines save_to_json_file function."""
import json


def save_to_json_file(my_obj, filename):
    """Saves object in filename as json object."""
    json_data = json.dumps(my_obj)
    with open(filename, "w") as file:
        file.write(json_data)
