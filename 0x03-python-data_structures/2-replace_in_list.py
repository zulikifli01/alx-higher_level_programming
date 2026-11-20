#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    for i, num in enumerate(my_list):
        if num == idx:
            my_list[i] = element
    return my_list
