#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        my_list.copy()
    elif idx > len(my_list) - 1:
        my_list.copy()
    else:
        my_list[idx] = element
