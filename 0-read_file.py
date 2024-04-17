#!/usr/bin/python3
"""
Module 0-read_file
Contains function that reads and prints from file
"""

def read_file(filename=""):
    """Read and print text from file"""
    with open(filename, mode="r", encoding="utf-8") as f:
        file_contents = f.read()
    print(file_contents, end="")

# Example usage:
# read_file("example.txt")