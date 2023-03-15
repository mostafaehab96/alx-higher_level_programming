#!/usr/bin/python3


def best_score(a_dictionary):
    try:
        return max(a_dictionary, key=a_dictionary.get)
    except (TypeError, AttributeError, ValueError):
        return None
