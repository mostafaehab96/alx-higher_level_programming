#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ != "__main__":
    exit(0)

if len(argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)

op = argv[2]
if op not in "+-*/":
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)

a = int(argv[1])
b = int(argv[3])

ops = {"+": add, "-": sub, "*": mul, "/": div}

print(f"{a} {op} {b} = {ops[op](a, b)}")
