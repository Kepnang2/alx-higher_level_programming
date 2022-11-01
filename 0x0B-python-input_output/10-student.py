#!/usr/bin/python3

""""
 class Student that defines a student
"""


class Student:
    """defines a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        new_dict = {}

        for key in attrs:
            try:
                new_dict[key] = self.__dict__[key]
            except Exception:
                pass

        return new_dict
