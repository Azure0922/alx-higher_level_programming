#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    y = len(my_list)
    if idx < y and idx > -1:
        my_list[idx] = []
        my_list
    else:
        return my_list
