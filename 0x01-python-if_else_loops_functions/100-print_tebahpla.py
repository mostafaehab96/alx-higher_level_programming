#!/usr/bin/python3

for c in range(ord('z'), ord('a') - 1, -1):
    print(chr(c) if c % 2 == 0 else chr(c).upper(), end="")
