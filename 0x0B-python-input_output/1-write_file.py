#!/usr/bin/python3
""" defines write file function """


def write_file(filename="", text=""):
    """ opens and writes """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
