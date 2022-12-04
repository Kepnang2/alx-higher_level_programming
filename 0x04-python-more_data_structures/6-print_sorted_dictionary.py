#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for element in sorted(a_dictionary.keys()):
        print("{:s}: {}".format(element, a_dictionary[element]))
