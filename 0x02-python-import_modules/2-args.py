#!/usr/bin/python3
from sys import argv as args


def main():
    size = len(args)
    if size > 2:
        print(f"{size - 1:d} arguments:")
    elif size == 2:
        print(f"1 argument:")
    else:
        print("0 arguments.")
    for i in range(1, size):
        print(f"{i:d}: {args[i]}")


if __name__ == "__main__":
    main()
