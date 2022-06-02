#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv


def main(lis):
    a = int(lis[1])
    op = lis[2]
    b = int(lis[3])
    if op == '+':
        print(f"{a:d} + {b:d} = {add(a, b)}")
    elif op == '/':
        print(f"{a:d} / {b:d} = {div(a, b)}")
    elif op == '-':
        print(f"{a:d} - {b:d} = {sub(a, b)}")
    elif op == '*':
        print(f"{a:d} * {b:d} = {mul(a, b)}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    main(argv)
