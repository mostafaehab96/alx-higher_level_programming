#!/usr/bin/python3

from dis import dis


def magic_calculation(a, b):
    result = 1
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            else:
                result += a ** b / i
        except Exception:
            result = a + b

        break

    return result
