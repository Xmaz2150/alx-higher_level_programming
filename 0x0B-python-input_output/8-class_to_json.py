#!/usr/bin/python3
""" defines class to json function """
from json import dumps


def class_to_json(obj):
    """ returns dict format of obj """
    return obj.__dict__
