#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    length = len(argv) - 1
    for i, arg in enumerate(argv):
        if i == 0:
            print(f"{length}", "argument" if length == 1 else "arguments",
                  end="")
            print("." if length == 0 else ":")
        else:
            print(f"{i}: {arg}")
