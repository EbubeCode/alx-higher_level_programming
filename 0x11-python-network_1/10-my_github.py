#!/usr/bin/python3
'''script that makes a get request on github'''
import requests
import sys

if __name__ == "__main__":
    u = ''
    p = ''
    if len(sys.argv) >= 2:
        u = sys.argv[1]
    if len(sys.argv) >= 3:
        p = sys.argv[2]
    url = 'https://api.github.com/user'
    res = requests.get(url, auth=(u, p))
    if res.status_code == 401:
        print('None')
    else:
        json = res.json()
        print(f"{json.get('id')}")
