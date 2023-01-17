#!/usr/bin/python3

"""
takes in a URL and an email, sends a POST request
"""

from urllib.request import urlopen
from urllib.parse import urlencode
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    data = urlencode(value)
    data = data.encode("ascii")

    with urlopen(url, data) as response:
        result = response.read().decode('utf-8')
        print(result)
