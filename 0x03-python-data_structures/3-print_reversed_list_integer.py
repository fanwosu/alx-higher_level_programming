#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    n = len(my_list)
    for i in range(1, n + 1):
        print("{:d}".format(my_list[-i]))
