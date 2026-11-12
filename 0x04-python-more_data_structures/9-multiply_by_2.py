#!/bin/env python
a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
x = 2


def multiply_by_2(a_dictionary):
    for key in a_dictionary:
        a_dictionary[key] *= x
    return a_dictionary


print(a_dictionary)
print("--------")
print(multiply_by_2(a_dictionary))


'''def multiply_by_2(dictionary,x):
    new = {}
    for key in a_dictionary:
        new[key] = a_dictionary[key] * x
    return new
print(multiply_by_2(a_dictionary,x))'''
