#!/usr/bin/python3
"""Adds items to json file from arguments."""
import json
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

args = sys.argv[1::]
try:
    py_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    save_to_json_file(args, "add_item.json")

else:
    py_list += args
    save_to_json_file(py_list, "add_item.json")
