#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    n = len(my_list)
    if idx < 0 or idx > n:
        return (my_list)
    for i in range(n):
        if idx == i:
            my_list.remove(idx)
    return (my_list)
