#!/usr/bin/python3
def fizzbuzz():
    x = range(1, 101)
    for n in x:
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz", end=' ')
        elif n % 3 == 0:
            print("Buzz", end=' ')
        elif n % 5 == 0:
            print("Fizz", end=' ')
        else:
            print(n, end=' ')
