#!/usr/bin/python3
x = range(122, 96, -1)
for n in x:
    y = chr(n)
if n % 2 == 1:
    n = n - 32
elif n % 2 == 0:
    n = n - 0
print("{y}".format(y = chr(n)), end= '')
