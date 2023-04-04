#!/usr/bin/python3

"""Defines a text_indentation function."""


def text_indentation(text):
    """A function text with 2 new lines after
    ., : and ?
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    word_begin = False
    for c in text:
        if c != " ":
            word_begin = True

        if c in ".:?":
            print(f"{c}\n")
            word_begin = False
        else:
            if word_begin:
                print(c, end="")
