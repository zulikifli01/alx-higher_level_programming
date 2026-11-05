#!/bin/env python
'''my_list = [1, 2, 3, 4, 5]
idx = 3

print("Element at index 3 is ",my_list[idx])'''


#!/bin/env python

def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]

my_list = [1, 2, 3, 4, 5]
idx = 3

my_list = element_at(my_list, idx)
print("Element at index 3 is", my_list)

