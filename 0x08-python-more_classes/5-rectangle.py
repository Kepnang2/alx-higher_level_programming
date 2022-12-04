#!/usr/bin/python3

"""
    Class the implements a rectangle
"""


class Rectangle:
    """Representation of a Rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        else:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        else:
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value

    def area(self):
        """
        Calculate area of the rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        calculates perimeter of the rectangle
        """

        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width + 2 * self.__height)

    def __str__(self):
        """print the rectangle with the character #"""
        if self.__width != 0 or self.__height != 0:
            string = ""
            string += "\n".join(["#" * self.__width for _ in
                                range(self.__height)])
        return (string)

    def __repr__(self):
        """return a string representation of the rectangle"""
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        """Print the message Bye rectangle"""
        print("Bye rectangle...")
        del self
