#!/usr/bin/python3
"""
    Matrix division: divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix by an integer or float
    Args:
        matrix (list): matrix to be divided
        div (int or float): the divisor
    Returns:
        a new matrix with the result
    """
    if matrix is None:
        raise TypeError("matrix must be a matrix (list of lists) of integers/\
floats")
    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/\
floats")
    if type(matrix) == set or type(matrix) == tuple:
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    for i in matrix:
        if len(i) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
        if type(i) == tuple or type(i) == set:
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if isinstance(div, int) is False and isinstance(div, float) is False:
        raise TypeError("div must be a number")
    length = len(matrix[0])
    for matrices in matrix:
        if len(matrices) != length:
            raise TypeError("Each row of the matrix must have the same size")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) != int and type(matrix[i][j]) != float:
                raise TypeError("matrix must be a matrix (list of lists) of\
 integers/floats")

    new_matrix = []
    for i in matrix:
        new_matrix.append(list(map(lambda x: round(x / div, 2), i)))
    return new_matrix
