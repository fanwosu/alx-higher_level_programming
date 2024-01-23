#!/usr/bin/python3
"""defines a square attribute: size and instantiation"""


class Square:
    """Defines a sqaure with private instance attribute"""

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be an integer")
        self.__size = size
