#!/usr/bin/python3

"""Defines a matrix_divided function."""


def matrix_divided(matrix, div):
    """Function that devides a matrix which is 
    a list of lists of integers or floats by div.
    """
    is_matrix = False
    is_all_int = False
    if matrix is not None:
        is_matrix = all([type(row) is list for row in matrix])
        if is_matrix:
            is_all_int = all([all([type(cell) is int or type(cell) is float\
                    for cell in row]) for row in matrix])
    
    if not is_matrix or not is_all_int:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    size = len(matrix[0])
    same_size = all([len(row) == size for row in matrix])
    if not same_size:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]

    

