#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    return ([list(map(lambda elm:elm * elm, list_a)) for list_a in matrix])
