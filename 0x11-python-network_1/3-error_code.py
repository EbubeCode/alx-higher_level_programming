#!/usr/bin/python3
'''script that fetches url and handles error'''

import urllib.request
import sys

if __name__ == "__main__":
    URL = sys.argv[1]
    try:
        with urllib.request.urlopen(URL) as res:
            m = res.read()
            print(m.decode())
    except urllib.error.HTTPError as e:
        print(f'Error code: {e.code}')
