#!/bin/env python
my_list = [1, 2, 3, 4, 5]
idx = 3

def delete_at(my_list=[], idx=3):
    if idx < len(my_list):
        del my_list[idx]

delete_at(my_list, idx)

print(my_list)
print(my_list)
