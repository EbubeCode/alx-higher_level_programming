#!/usr/bin/python3
'''script that a post request'''
import requests
import sys

if __name__ == "__main__":
    e = sys.argv[2]
    res = requests.post(sys.argv[1], data={'email': e})
    print(res.content.decode())
