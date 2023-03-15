#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_value = max(a_dictionary.values())
    if max_value is None:
        return None
    return [k for k, v in a_dictionary.items() if v == max_value][0]
