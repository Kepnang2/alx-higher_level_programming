#!/usr/bin/python3

"""
    This is the 0-add_integer Module
    This 0-add_interger Module supplies one function, add_integer(a, b)
"""

def add_integer(a, b=98):
    """Return the addition of two numbers"""

    if not isinstance(a,(int,float)):
        raise TypeError("a must be an integer")
    else:
        a = int(a)
    if not isinstance(b,(int,float)):  
        raise TypeError("b must be an integer")
    else:
        b = int(b)
    return (a + b)
