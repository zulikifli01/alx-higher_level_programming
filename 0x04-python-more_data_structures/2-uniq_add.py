#!/bin/env python
my_list = [1, 2, 3, 1, 4, 2, 5]
def uniq_add(my_list=[]):
    result = sum(set(my_list))
    return result
print("Result: ", uniq_add(my_list))
