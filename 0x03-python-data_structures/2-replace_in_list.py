#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if my_list is not None:
        length = len(my_list)
        if not idx < 0 or not idx >= length:
            my_list[idx] = element
    return my_list
