#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    y = len(my_list)
    n = my_list[:]
    for i in range(y):
        if my_list[i]% 2 == 0:
            n = True
        else:
            n = False
        return n
