#!/bin/env python
def max_integer(my_list=[]):
    my_max = my_list[0]
    
    for x in my_list:
        if x>my_max:
            my_max = x

    return my_max





my_list = [1, 90, 2, 13, 34, 5, -13, 3]
# print(my_list)
max_value = max_integer(my_list)
print("Max:", max_value)
# print("Max: {}".format(max_value))
