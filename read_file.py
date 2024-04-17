#!/usr/bin/python3
"""
Module read_file
Contains function that reads and returns contents of a file
"""

def read_file(filename=""):
    """Read and return the contents of the specified file"""
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

# Example usage:
# contents = read_file("example.txt")
# print(contents)
