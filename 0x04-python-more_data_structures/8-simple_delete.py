#!/bin/env python
def simple_delete(a_dictionary, key=""):
    a_dictionary = {k: v for k, v in a_dictionary.items() if k != 'ids'}
    print(a_dictionary)
