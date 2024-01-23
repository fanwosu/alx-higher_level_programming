#!/usr/bin/python3
"""defines a square attribute: size and instantiation"""


class Square:
    """Defines a sqaure with private instance attribute"""
    def __init__(self, size=0):
        self.__size = size
        try:
            print("{:d}".format(size))
            try:
                size < 0
            except ValueError:
                print("size must be >= 0")
        except TypeError:
            print("size must be an integer")
