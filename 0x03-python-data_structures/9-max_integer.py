#!/usr/bin/python3

def max_integer(my_list=[]):
    n = len(my_list)
    if n == 0:
        return (None)
    max = my_list[0]
    for i in range(n):
        if my_list[i] > max:
            max = my_list[i]
    return (max)
