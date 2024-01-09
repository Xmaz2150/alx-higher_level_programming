#!/usr/bin/python3
""" dedfines append write function """


def append_write(filename="", text=""):
    """ appends to file """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
