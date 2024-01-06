#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list_copy = []
    if idx <= 0:
        for i in range(len(my_list)):
            my_list_copy = my_list[i]
        return (my_list_copy)
    if idx > len(my_list):
        for i in range(len(my_list)):
            my_list_copy = my_list[i]
        return (my_list_copy)
    for i in range(len(my_list)):
        if i != idx:
            my_list_copy.append(my_list[i])
        else:
            my_list_copy.append(element)
    return (my_list_copy)
