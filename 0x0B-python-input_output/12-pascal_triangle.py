#!/usr/bin/python3
"""module for paschal triangle"""


def pascal_triangle(n):
    """method for pascal triangle"""
    if n <= 0:
        return []
    pasc = []
    for i in range(1, n+1):
        line = [1]
        if i == 1:
            pasc.append(line)
            continue
        prev = pasc[i - 2]
        for j in range(i - 2):
            line.append(prev[j] + prev[j + 1])
        line.append(1)
        pasc.append(line)
    return pasc
