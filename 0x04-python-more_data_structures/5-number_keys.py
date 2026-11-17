#!/bin/env python
'''def number_keys(a_dictionary):
    leng = sum(1 for _ in a_dictionary)
    print('Number of keys: ', leng)'''

def number_keys(a_dictionary):
    leng = len(a_dictionary.keys())
    print("Number of keys:", leng)
