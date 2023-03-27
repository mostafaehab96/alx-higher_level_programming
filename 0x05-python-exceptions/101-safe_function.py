#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    result = None
    try:
        result = fct(*args)
    except Exception as exc:
        print("Exception: {}".format(exc), file=stderr)

    return result
