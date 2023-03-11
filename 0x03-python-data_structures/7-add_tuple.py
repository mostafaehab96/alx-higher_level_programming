#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    a_len = len(tuple_a) if tuple_a is not None else 0
    b_len = len(tuple_b) if tuple_b is not None else 0
    a_0 = tuple_a[0] if a_len > 0 else 0
    a_1 = tuple_a[1] if a_len > 1 else 0
    b_0 = tuple_b[0] if b_len > 0 else 0
    b_1 = tuple_b[1] if b_len > 1 else 0

    return (a_0 + b_0, a_1 + b_1)
