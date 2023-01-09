#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    y = len(my_list)
    if idx < y + 1 and idx > 0:
        del my_list[idx]
    else:
        return my_list
