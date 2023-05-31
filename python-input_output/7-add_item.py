#!/usr/bin/python3
"""
Script that add all arguments to a list
"""
import sys
load = __import__("6-load_from_json_file").load_from_json_file
save = __import__("5-save_to_json_file").save_to_json_file


try:
    pythonList = load("add_item.json")

except(TypeError, FileNotFoundError):
    pythonList = []

for i in sys.argv[1:]:
    pythonList.append(i)

save(pythonList, "add_item.json")
