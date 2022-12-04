#!/usr/bin/python3

def search_replace(my_list, search, replace):
    def replace_it(element):
        return (element if element != search else replace)
    return(list(map(replace_it, my_list)))
