#!/usr/bin/python3
def element_at(my_list, idx):
    y = len(my_list)
    if idx < 0:
        return None
    elif idx > y - 1:
        return None
    else:
        z = my_list[idx]
        return z
