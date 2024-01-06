#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    n = len(my_list)
    if n == 0:
        return (None)
    new_list = my_list[:]
    for i in range(n):
        if my_list[i] % 2 == 0:
            new_list[i] = True
        else:
            new_list[i] = False
    return (new_list)
