#!/bin/env python
a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3] }


def simple_delete(a_dictionary, key=""):
    a_dictionary = {k: v for k, v in a_dictionary.items() if k != 'ids'}
    print(a_dictionary)


simple_delete(a_dictionary, key="")

'''rmv  = a_dictionary.pop('track')
print(a_dictionary)
# print(rmv)'''
