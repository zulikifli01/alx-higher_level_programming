#!/bin/env python
def no_c(my_string):
    new_string = ''
    for c in my_string:
        if c.lower() != 'c':
            new_string += c
    return new_string
print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
