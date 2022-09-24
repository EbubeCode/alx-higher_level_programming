#!/usr/bin/python3
'''script that fetches https://alx-intranet.hbtn.io/status'''

import requests

if __name__ == "__main__":
    res = requests.get('https://alx-intranet.hbtn.io/status')
    mess = res.content.decode()
    print('Body response:')
    print(f"\t- type: {type(mess)}")
    print(f"\t- content: {mess}")
