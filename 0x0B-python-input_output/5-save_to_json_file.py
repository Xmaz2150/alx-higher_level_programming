#!/usr/bin/python3
""" defines save to json file """
to_json_string = __import__('3-to_json_string').to_json_string


def save_to_json_file(my_obj, filename):
    """ writes json representation of my_obj """
    my_json = to_json_string(my_obj)
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(my_json)
