#!/bin/env python
my_list = [0, 1, 2, 3, 4, 5, 6]
def divisible_by_2(my_list=[]):
    new_list = []
    for i in my_list:
        if i % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
new_list = divisible_by_2(my_list)
print(new_list)
