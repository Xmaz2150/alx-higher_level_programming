#!/usr/bin/python3
""" defines load from json file function """
from_json_string = __import__('4-from_json_string').from_json_string


def load_from_json_file(filename):
    """ returns obj derived from json str filename """
    with open(filename, 'r', encoding="utf-8") as f:
        return from_json_string(f.read())
