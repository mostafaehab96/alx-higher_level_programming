#!/usr/bin/python3


def best_score(a_dictionary):
    try:
        max_value = max(a_dictionary.values())
    except (TypeError, AttributeError):
        return None
    return [k for k, v in a_dictionary.items() if v == max_value][0]
