#!/usr/bin/python3
'''script that makes a get request on github'''
import requests
import sys

if __name__ == "__main__":
    owner = ''
    repo = ''
    if len(sys.argv) >= 2:
        repo = sys.argv[1]
    if len(sys.argv) >= 3:
        owner = sys.argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    res = requests.get(url)
    if res.status_code == 200:
        json = res.json()[:10]
        for c in json[:10]:
            name = c.get('commit').get('author').get('name')
            print(f"{c.get('sha')}: {name}")
