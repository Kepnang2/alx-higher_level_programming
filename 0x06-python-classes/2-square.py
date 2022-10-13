#!/usr/bin/python3

"""class square - Describes a square"""


class Square:
    """Represents a square
    Attributes
    size which is size of the sides og a square
    """

    def __init__(self, size=0):

        """Intializes the square
        Args:size (int): size of a side of the square
        Returns:None
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        else:
            if (size < 0):
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
