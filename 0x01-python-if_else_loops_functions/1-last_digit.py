#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
val = abs(number)
unit = val % 10
if unit > 5:
    print(f"Last digit of {number} is {unit} and is greater than 5")
elif unit == 0:
    print(f"Last digit of {number} is {unit} and is 0")
elif unit < 6 and not 0:
    print(f"Last digit of {number} is {unit} and is less than 6 and not 0")
