#!/usr/bin/python3

def uppercase(str):
    new_str = ''
    for letter in str:
        if(ord(letter) in range(ord('a'), ord('z')+1)):
            letter = chr(ord(letter)-(ord('a')-ord('A')))
            new_str += letter
        else:
            new_str += letter
    print("{:s}".format(new_str))
