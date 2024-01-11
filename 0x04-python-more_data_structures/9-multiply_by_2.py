#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    result = {}
    for key in a_dictionary:
        value = a_dictionary[key] * 2
        result[key] = value
    return (result)
