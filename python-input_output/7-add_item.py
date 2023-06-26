#!/usr/bin/python3
"""
This program take the file add_item.json, and add the
parameters to the list inside this file.

- If the file doesn't exist create it.
- If no exist parameters do nothing or create the list if the file is empty.
"""


from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    existing_content = load_from_json_file(filename)
except FileNotFoundError:
    existing_content = []

save_to_json_file(existing_content + argv[1:], filename)
