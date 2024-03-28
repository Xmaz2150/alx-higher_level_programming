#!/usr/bin/python3
""" sends request to URL and display value of X-Request-Id
    variable in header response
"""
import urllib.request
import sys

if len(sys.argv) < 2:
    exit(1)
else:
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers.get('X-Request-Id'))
