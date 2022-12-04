#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        sum = 0
        weights = 0

        for tuple in my_list:
            sum += (tuple[0] * tuple[1])
            weights += tuple[1]

        return (sum/weights)
    return 0
