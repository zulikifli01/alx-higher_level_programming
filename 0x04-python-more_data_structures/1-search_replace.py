#!/bin/env python
my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
search = 2
replace = 89
new_list = my_list.copy()

def search_replace(my_list, search, replace):
    for i in range(len(my_list)):
        if my_list[i] == search:
            my_list[i] = replace
    return my_list


search_replace(my_list, search, replace)
print(my_list)
print(new_list)
