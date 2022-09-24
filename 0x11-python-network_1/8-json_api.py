#!/usr/bin/python3
'''script that makes a post request'''
import requests
import sys

if __name__ == "__main__":
    q = ''
    if len(sys.argv) >= 2:
        q = sys.argv[1]
    url = 'http://0.0.0.0:5000/search_user'
    res = requests.post(url, data={'q': q})
    try:
        json = res.json()
        if len(json) == 0:
            print('No result')
        else:
            print(f"[{json.get('id')}] {json.get('name')}")
    except ValueError as e:
        print('Not a valid JSON')
