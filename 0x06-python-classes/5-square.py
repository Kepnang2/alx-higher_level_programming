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
        self.__size = size

    def area(self):
        """ Finds area of the square
        Args:
            None
        Returns:
            Area of the square
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        else:
            if (value < 0):
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def my_print(self):
        if (self.__size == 0):
            print()
        else:
            for element in range(self.__size):
                for element in range(self.__size):
                    print('#', end='')
                print()
