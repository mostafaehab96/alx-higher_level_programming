#!/usr/bin/python3
def magic_string(dic={"i": 0}):
    dic['i'] += 1
    return ("BestSchool, " * dic['i'])[:-2]
