#!/usr/bin/python3
x = range(122, 97, -1)
for n in x:
    if n % 2 == 1:
        n = n - 32
    elif n % 2 == 0:
        n = n - 0
y = chr(n)
print(y, end= '')
