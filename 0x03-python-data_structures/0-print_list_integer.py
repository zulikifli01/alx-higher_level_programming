#!/bin/env python
def print_list_integer(my_list=[]):
    for i in my_list:
        print("{:.0f}".format(i))

my_list=[1, 2, 3, 4, 5]
print_list_integer(my_list)
