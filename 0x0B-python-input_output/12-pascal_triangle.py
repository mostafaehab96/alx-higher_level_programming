#!/usr/bin/python3
"""Pascal's triangle function."""


def factorial(num):
    """Returns factorial of number."""
    if num < 2:
        return 1
    return num * factorial(num - 1)


def coeff(n, r):
    """Returns the coeffecient of number."""
    return factorial(n) // (factorial((n-r)) * factorial(r))


def pascal_triangle(n):
    """Returns a list of pascal triangle."""
    if n <= 0:
        return []
    pascal = []
    for i in range(n):
        inner = []
        for j in range(i + 1):
            inner.append(coeff(i, j))
        pascal.append(inner)

    return pascal
