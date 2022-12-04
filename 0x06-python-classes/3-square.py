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

    def area(self):
        """ Finds area of the square
        Args:
            None
        Returns:
            Area of the square
        """
        return (self.__size * self.__size)
