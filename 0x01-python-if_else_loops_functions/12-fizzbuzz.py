#!/usr/bin/python3
def fizzbuzz():
    for n in range(1, 101):
        if n % 3 == 0 and n % 5 == 0:
            n = "FizzBuzz"
        elif n % 3 == 0:
            n = "Buzz"
        elif n % 5 == 0:
            n = "Fizz"
        else:
            n = n
    print(n, end= ' ')
