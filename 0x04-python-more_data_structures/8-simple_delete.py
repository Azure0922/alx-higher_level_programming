#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for n in a_dictionary:
        if n == key:
            del a_dictionary[key]
    return a_dictionary
