#!/usr/bin/python3
""" defines is kind of class function """


def is_kind_of_class(obj, a_class):
    """ checks if obj is instance of a_class
        or
        if obj is instance inherited from a_class
    """
    if isinstance(obj, a_class):
        return True
    elif issubclass(type(obj), a_class):
        return True
    else:
        return False
