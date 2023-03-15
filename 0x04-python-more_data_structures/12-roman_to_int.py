#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    previous = ''
    for c in roman_string:
        if previous == '':
            previous = c
            continue
        else:
            p_value = romans[previous]
            c_value = romans[c]
            if c_value > p_value:
                result += (c_value - p_value)
            else:
                result += (c_value + p_value)
            previous = ''

    result += romans.get(previous, 0)
    return result
