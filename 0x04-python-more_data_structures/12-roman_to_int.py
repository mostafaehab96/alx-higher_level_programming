#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    c_vlaue = 0
    p_value = 0

    for c in roman_string:
        c_value = romans.get(c, 0)
        if c_value <= p_value:
            result += p_value
        else:
            result -= p_value
        p_value = c_value

    result += p_value
    return result
