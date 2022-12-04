#!/usr/bin/python3
"""draw a pascal triangle"""


def pascal_triangle(n):
    """
        returns a list of lists of integers
        representing the Pascal’s triangle of n
    """
    my_list = [[0 for j in range(i + 1)] for i in range(n)]
    for i in range(n):
        for j in range(i + 1):
            if j == 0:
                my_list[i][j] = 1
            elif j == i:
                my_list[i][j] = 1
            else:
                my_list[i][j] = my_list[i-1][j] + my_list[i-1][j-1]
    return my_list
