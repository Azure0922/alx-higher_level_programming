#!/usr/bin/python3
def uppercase(str):
    if ord(str) >= 65 and <= 90:
        print(str)
    elif ord(str) >= 97 and <= 122:
        x = ord(str) - 32
        print(chr(x))
    else:
        print(str)
