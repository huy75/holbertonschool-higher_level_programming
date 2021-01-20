#!/usr/bin/python3
# 6-load_from_json_file.py
"""
Defines a JSON file-reading function.
"""
import json


def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file.
    """
    with open(filename) as f:
        return json.load(f)
