#!/usr/bin/python3

def remove_char_at(str, n):
    for i in range(len(str)):
        if i == n:
            str = str[:i] + str[i + 1:]
            return str

    return str
