#!/usr/bin/python3
x = range(97, 101)
y = range(102, 113)
z = range(114, 123)
i = list(x) + list(y) + list(z)
for n in i:
    print("{a}".format(a = chr(n)), end= '')
