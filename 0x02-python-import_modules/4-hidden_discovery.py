#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    lis = dir(hidden_4)
    for s in lis:
        if not s.startswith("__"):
            print(s)
