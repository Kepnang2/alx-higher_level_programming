#!/usr/bin/python3
"""
takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
from sys import argv

if __name__ == "__main__":
    name = argv[1]
    token = argv[2]
    credt = (name, token)
    url = "https://api.github.com/user"

    response = requests.get(url, auth=credt)
    response = response.json()
    print(response.get('id'))
