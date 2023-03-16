#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    c_vlaue = ''
    p_value = ''
    for i in range(len(roman_string)):
        c_value = romans[roman_string[i]]
        if i > 0:
            p_value = romans[roman_string[i - 1]]
            if p_value < c_value:
                result += (c_value - (p_value * 2))
            else:
                result += c_value
        else:
            result += c_value

    return result
