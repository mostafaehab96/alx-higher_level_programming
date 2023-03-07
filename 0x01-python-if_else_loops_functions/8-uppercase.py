#!/usr/bin/python3

def uppercase(s):
    for c in s:
        valid = c.isalpha() and c.islower()
        print("{}".format(chr(ord(c) - 32) if valid else c), end="")
    print()
