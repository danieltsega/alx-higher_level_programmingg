#!/usr/bin/python3
def islower(a):
    a = ord(a)
    if a >= 0 and a <= 90:
        return False
    elif a >= 97 and a <= 127:
        return True
