#!/bin/env python
'''my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)'''

'''my_list = [1, 2, 3, 4, 5]
for x in reversed(my_list):
    print(x)'''

def print_reversed_list_integer(my_list=[]):
    if my_list:
        for i in reversed(my_list):
            print("{:d}".format(i))

print_reversed_list_integer(my_list = [1, 2, 3, 4, 5])
