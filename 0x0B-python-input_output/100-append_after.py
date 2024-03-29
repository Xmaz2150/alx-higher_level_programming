#!/usr/bin/python3
""" defines append after function """


def append_after(filename="", search_string="", new_string=""):
    """ search and update """
    with open(filename, 'r+') as f:
        lines = f.readlines()
        i = 0
        for line in lines:
            if line.find(search_string) is not -1:
                lines.insert(i + 1, new_string)
            i += 1
        f.seek(0)
        f.write("".join(lines))
