#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    y = len(my_list)
    if idx < 0:
        return None
    elif idx > y - 1:
        return None
    else:
        my_list[idx] = element
        return my_list
