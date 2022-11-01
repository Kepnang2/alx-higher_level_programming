#!/usr/bin/python3
"""insert a line of text"""


def append_after(filename="", search_string="", new_string=""):
    """
        serts a line of text to a file, after each line
        containing a specific string (see example)
        Args:
            filename (str): input file
            search_string (str): string to be searched
            new_string (str): string to be appended
    """
    lines = ""
    with open(filename, encoding="utf-8", mode="r") as f:
        readline = f.readline()
        while readline:
            lines += readline
            if search_string in readline:
                lines += new_string
            readline = f.readline()
    with open(filename, encoding="utf-8", mode="w") as f:
        f.write(lines)
