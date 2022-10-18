#!/usr/bin/python3
"""Document about say_my_name function"""


def say_my_name(first_name, last_name=""):
    """say the first name
    Args:
        first_name (str): first name
        last_name (str, optional): last name
    Raises:
        TypeError: if any args is not a string
    """

    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
