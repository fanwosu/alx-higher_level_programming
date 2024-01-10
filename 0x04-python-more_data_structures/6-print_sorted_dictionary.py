#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dic = sorted(a_dictionary)
    for key in sorted_dic:
        value = a_dictionary[key]
        print(f"{key}: {value}")
