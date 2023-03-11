#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    length = len(my_list)
    if not idx < 0 and not idx >= length:
        my_list[idx] = element
    return my_list
