#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        x = abs(number)
        y = x % 10
        return y * -1
    else:
        z = number % 10
        return z
