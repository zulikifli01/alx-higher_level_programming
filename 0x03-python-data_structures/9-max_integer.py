#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    my_max = my_list[0]
    for x in my_list:
        if x > my_max:
            my_max = x

    return my_max
