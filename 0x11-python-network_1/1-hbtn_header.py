#!/usr/bin/python3
'''script that finds the X-Request-Id header for URL'''

import urllib.request
import sys

if __name__ == "__main__":
    URL = sys.argv[1]
    with urllib.request.urlopen(URL) as res:
        h = res.info().get('X-Request-Id')
        print(h)
