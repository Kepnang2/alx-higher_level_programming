#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map((lambda lis: list(map((lambda x: x * x), lis))), matrix))
