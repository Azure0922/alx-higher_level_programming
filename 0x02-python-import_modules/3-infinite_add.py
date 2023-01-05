#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    x = len(sys.argv)
    total = 0
    for i in range(1, x):
        total = total + int(str(sys.argv[i]))
    print(total)
