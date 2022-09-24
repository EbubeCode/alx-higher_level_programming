#!/usr/bin/python3
'''script that finds the X-Request-Id header for URL'''

import requests
import sys

if __name__ == "__main__":
    URL = sys.argv[1]
    with requests.get(URL) as res:
        h = res.headers['X-Request-Id']
        print(h)
