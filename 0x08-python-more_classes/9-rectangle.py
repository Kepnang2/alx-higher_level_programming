#!/usr/bin/python3

"""
    Class the implements a rectangle
"""


class Rectangle:
    """Representation of a Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2
        return rect_1

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            string += "\n".join([str(self.print_symbol) * self.__width for _ in
                                range(self.__height)])
        return (string)

    def __repr__(self):
        """return a string representation of the rectangle"""
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        """Print the message Bye rectangle"""
        print("Bye rectangle...")
        del self
        Rectangle.number_of_instances -= 1
