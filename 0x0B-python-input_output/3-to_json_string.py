#!/usr/bin/python3
""" to json string function """
from json import dumps


def to_json_string(my_obj):
    """ returns json representaion of obj """
    return dumps(my_obj)
