#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    y = len(my_list)
    if idx < 0:
        return my_list
    elif idx > y - 1:
        return my_list
    elif idx > 0 and idx < y + 1:
        my_list[idx] = element
    return my_list
