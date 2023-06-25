#!/usr/bin/python3
"""
class that inherits the attributes of list
"""


class MyList(list):
    """inherits from the list"""
    def print_sorted(self):
        """puclic instance printing ordered list of integers"""
        print(sorted(self))
