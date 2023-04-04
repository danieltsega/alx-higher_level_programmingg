#!/usr/bin/python3
"""A Matrix dividing module"""


def matrix_divided(matrix, div):
    """A function that divides a given
    matrix by the variable div
    """

    err_type = "matrix must be a matrix (list of lists) of integers/floats"
    err_size = "Each row of the matrix must have the same size"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(err_type)

    element_len = 0
    for element in matrix:
        if not element or not isinstance(element, list):
            raise TypeError(err_type)
        if element_len != 0 and len(element) != element_len:
            raise TypeError(err_size)

        for i in element:
            if not type(i) in (int, float):
                raise TypeError(err_type)

        element_len = len(element)

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    z = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return z
