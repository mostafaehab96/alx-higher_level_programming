#!/usr/bin/python3

def uppercase(s):
    for c in s:
        print("{}".format(chr(ord(c) - 32) if c.isalpha() and c.islower() else c), end="")
    print()

