#!/usr/bin/python3
# script that fetches https://alx-intranet.hbtn.io/status

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        mess = res.read()
        print('Body response:')
        print(f"\t- type: {type(mess)}")
        print(f"\t- content: {mess}")
        print(f"\t- utf8 content: {mess.decode()}")
