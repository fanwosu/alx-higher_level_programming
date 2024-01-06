#!/usr/bin/python3

def max_integer(my_list=[]):
    n = len(my_list)
    max = my_list[0]
    if n == 0:
        return ('None')
    for i in range(n):
        if my_list[i] > max:
            max = my_list[i]
    return (max)
