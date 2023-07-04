#!/usr/bin/python3
'''
Module: '5-hbtn_header'
Displays the value of variable in the response header
'''

import requests
from sys import argv

if __name__ == '__main__':
    with requests.get(argv[1]) as response:
        header = response.headers.get('X-Request-Id')
    print(header)
