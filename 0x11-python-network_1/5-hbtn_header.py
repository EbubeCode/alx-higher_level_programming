#!/usr/bin/python3
'''script that finds the X-Request-Id header for URL'''
import requests
import sys

if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    print(res.headers.get('X-Request-Id'))
