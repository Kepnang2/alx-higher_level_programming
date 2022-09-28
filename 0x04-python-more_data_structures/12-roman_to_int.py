#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    d_1 = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100,
           "XC": 90, "L": 50, "XL": 40, "X": 10, "V": 5, "IV": 4, "I": 1}
    res = 0
    for i in range(len(roman_string)):
        if i > 0 and d_1[roman_string[i]] > d_1[roman_string[i - 1]]:
            res += d_1[roman_string[i]] - 2 * d_1[roman_string[i - 1]]
        else:
            res += d_1[roman_string[i]]
    return res
