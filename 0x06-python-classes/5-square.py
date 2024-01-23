#!/usr/bin/python3
"""defines a square attribute: size and instantiation"""


class Square:
    """Defines a sqaure with private instance attribute"""

    res = 0

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        self.__size = value

    def area(self):
        """calculates and returns current square area"""

        return (self.__size ** 2)

    def my_print(self):
         """prints square of size self.__size using #"""

         if self.__size > 0:
             for column in range(self.__size):
                 for row in range(self.__size):
                     print("#", end="")
                 print()
         else:
             print()
