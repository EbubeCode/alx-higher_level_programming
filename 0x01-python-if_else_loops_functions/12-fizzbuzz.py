#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        e = ' '
        if i % 15 == 0:
            print('FizzBuzz', end=e)
        elif i % 5 == 0:
            print('Buzz', end=e)
        elif i % 3 == 0:
            print('Fizz', end=e)
        else:
            print(i, end=e)
