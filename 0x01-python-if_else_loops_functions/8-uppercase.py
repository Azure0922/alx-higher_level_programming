#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 65 and ord(str[i]) <= 90:
            print("{a}".format(a=str[i]), end='')
        elif ord(str[i]) >= 97 and ord(str[i]) <= 122:
            x = ord(str) - 32
            print("{p}".format(chr(x)), end='')
        else:
            print(str, end='')
    print()
