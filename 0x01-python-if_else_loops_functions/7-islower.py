#!/usr/bin/python3
def islower(c):
    for letter in range(ord('a'), ord('z')):
        if(letter == ord(c)):
            return True
    return False
