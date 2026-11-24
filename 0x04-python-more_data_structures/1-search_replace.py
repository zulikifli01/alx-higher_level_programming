#!/usr/bin/python3
'''def search_replace(my_list, search, replace):
    new_list = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            my_list[i] = replace
    return my_list'''


def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for idx, item in enumerate(new_list):
        if item == search:
            new_list[idx] = replace
    return new_list
