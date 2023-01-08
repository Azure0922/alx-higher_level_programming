#!/usr/bin/python3
def max_integer(my_list=[]):
    y = len(my_list)
    if y == 0:
        return None
    else:
        for n in my_list:
            max = 0
            if my_list[n] > max:
                max = my_list[n]
