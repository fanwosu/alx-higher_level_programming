#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_my_list = set();
    for i in my_list:
        unique_my_list.add(i)
        result = sum(unique_my_list)
    return (result)  
