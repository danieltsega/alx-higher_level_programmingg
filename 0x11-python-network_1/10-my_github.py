#!/usr/bin/python3
'''
Module: '10-my_github'
Script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
'''
import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(url, auth=(username, password))
    try:
        print(response.json().get('id'))
    except ValueError:
        print("None")
