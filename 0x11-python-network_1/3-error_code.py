#!/usr/bin/python3
"""
takes in a URL, returns response on success or error
"""
from urllib.request import urlopen
from urllib.error import HTTPError
from sys import argv

if __name__ == "__main__":
    try:
        with urlopen(argv[1]) as response:
            result = response.read().decode("utf-8")
            print(result)
    except HTTPError as e:
        print(f"Error code: {e.code}")
