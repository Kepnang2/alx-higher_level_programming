#!/usr/bin/python3
""" prints a square with the # char """


def print_square(size):
    """
    prints a square
    Args: Size
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        if size == 0:
            return
        else:
            for _ in range(size):
                [print("#", end="") for _ in range(size)]
                print("")
