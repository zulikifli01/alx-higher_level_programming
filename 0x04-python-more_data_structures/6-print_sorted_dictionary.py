#!/bin/env python
a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }


def print_sorted_dictionary(a_dictionary):
    for key, value in sorted(a_dictionary.items(), key=lambda x: x[0]):
        print("{} : {}".format(key, value))


print_sorted_dictionary(a_dictionary)

'''def print_sorted_dictionary(a_dictionary):
    asc = {k: v for k, v in sorted(a_dictionary.items(), key=lambda item: item[0])}
    print(asc, end=" ")

print_sorted_dictionary(a_dictionary)'''
'''def print_sorted_dictionary(a_dictionary):
    for key, value in sorted(a_dictionary.items()):
        print("{} : {}".format(key, value))


print_sorted_dictionary(a_dictionary)'''
