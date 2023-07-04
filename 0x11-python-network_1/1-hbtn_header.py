#!/usr/bin/python3
'''
Module: '1-hbtn_header'
Displays the value of the X-Request-Id variable found in the header response
'''

import urllib.request
from sys import argv
if __name__ == '__main__':
    with urllib.request.urlopen(argv[1]) as response:
        header = response.getheader('X-Request-Id')

    print(header)
