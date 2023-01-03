#!/usr/bin/python3
x = range(0, 100)
for n in x:
    if n < 99:
        print("{:0>2d}".format(n), end=', ')
    else:
        print("{a}".format(a=n))
