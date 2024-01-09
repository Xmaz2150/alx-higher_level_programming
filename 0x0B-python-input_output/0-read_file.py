#!/usr/bin/python3
""" defines read file function """


def read_file(filename=""):
    with open(filename, 'r') as f:
        print(f.read())
