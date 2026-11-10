#!/bin/env python
a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }


def number_keys(a_dictionary):
    leng = sum(1 for _ in a_dictionary)
    print('Number of keys: ', leng)


number_keys(a_dictionary)

'''def number_keys(a_dictionary):
    leng = len(a_dictionary.keys())
    print(leng)
number_keys(a_dictionary)'''
