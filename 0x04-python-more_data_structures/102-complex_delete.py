#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    deleted_keys = []

    for key in a_dictionary.keys():
        if (a_dictionary[key] == value):
            deleted_keys.append(key)
    for item in deleted_keys:
        del a_dictionary[item]
    return a_dictionary
