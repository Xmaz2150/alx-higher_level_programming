#!/usr/bin/python3
""" adds all args to json """
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


new_list = argv[1:]
filename = "add_item.json"

try:
    old_list = load_from_json_file(filename)
except FileNotFoundError:
    old_list = []

old_list += new_list
save_to_json_file(old_list, filename)
