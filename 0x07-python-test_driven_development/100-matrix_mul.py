#!/usr/bin/python3

"""Defines a matrix multiplication function
and a checker function for validation
"""


def validate(matrix, name):
    """Validate the matrix is valid
    for multiplication
    """

    is_matrix = False
    is_all_num = False
    if matrix is not None and type(matrix) is list:
        is_matrix = all([type(row) is list for row in matrix])
        if is_matrix:
            is_all_num = (all([all([type(cell) is int or type(cell) is float
                                    for cell in row]) for row in matrix]))
    else:
        raise TypeError(f"{name} must be a list")

    if not is_matrix:
        raise TypeError(f"{name} must be a list of lists")
    if len(matrix) == 0 or any([len(row) == 0 for row in matrix]):
        raise ValueError(f"{name} can't be empty")
    if not is_all_num:
        raise TypeError(f"{matrix} should contain only integers or floats")

    size = len(matrix[0])
    if not all([len(row) == size for row in matrix]):
        raise TypeError(f"each row of {name} must be of the same size")


def matrix_mul(m_a, m_b):
    """Multiply two matrices."""
    validate(m_a, "m_a")
    validate(m_b, "m_b")
    cols_a = len(m_a[0])
    rows_b = len(m_b)
    if cols_a != rows_b:
        raise ValueError("m_a and m_b can't be multiplied")

    result_matrix = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            result = 0
            for c in range(rows_b):
                result += m_a[i][c] * m_b[c][j]

            row.append(result)

        result_matrix.append(row)

    return (result_matrix)
