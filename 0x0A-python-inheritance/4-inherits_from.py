#!/usr/bin/python3
""" defines inherits from function """


def inherits_from(obj, a_class):
    """ checks if obj is instance of a_class
        after checking
        if obj is instance inherited from a_class
    """
    if issubclass(type(obj), a_class):
        return isinstance(obj, a_class)
    else:
        return False
