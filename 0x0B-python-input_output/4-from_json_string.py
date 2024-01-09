#!/usr/bin/python3
""" defines from jason string function """
from json import loads


def from_json_string(my_str):
    """ creates python obj from json str """
    return loads(my_str)
