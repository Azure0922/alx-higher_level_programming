#!/usr/bin/python3
x = range(0, 100)
for n in x:
    if n < 99:
        print(f"{n:02}", end= ', ')
    else:
        print(n)
