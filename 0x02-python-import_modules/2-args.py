#!/usr/bin/python3
import sys
if __name__ == '__main__':
    x = len(sys.argv)
    if x == 1:
        print("0 arguments.")
    elif x > 1:
        print(x - 1, " arguments:")
        for i in range(1, x):
            print(i, " : ", str(sys.argv[i]))
