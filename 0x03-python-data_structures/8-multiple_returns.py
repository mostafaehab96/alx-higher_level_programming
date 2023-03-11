#!/usr/bin/python3


def multiple_returns(sentence):
    length = len(sentence) if sentence is not None else 0
    first = sentence[0] if length != 0 else None
    return (length, first)
