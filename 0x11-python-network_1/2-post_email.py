#!/usr/bin/python3
'''
Module: '2-post_email'
Sends the POST request andbdisplays the body of the response
'''
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))
