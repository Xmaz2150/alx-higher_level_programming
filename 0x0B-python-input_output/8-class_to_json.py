#!/usr/bin/python3
""" defines class to json function """


def class_to_json(obj):
    """ returns dict format of obj """
    return obj.__dict__
