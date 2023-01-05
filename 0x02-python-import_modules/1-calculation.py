#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
c = add(a, b)
d = sub(a, b)
e = mul(a, b)
f = div(a, b)
if __name__ == '__main__':
    print("{g} + {h} = {i}".format(g=a, h=b, i=c))
    print("{g} - {h} = {i}".format(g=a, h=b, i=d))
    print("{g} * {h} = {i}".format(g=a, h=b, i=e))
    print("{g} / {h} = {i}".format(g=a, h=b, i=f))
