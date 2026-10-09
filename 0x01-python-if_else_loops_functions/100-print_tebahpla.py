#!/bin/env python
"""for i in range(97, 123):
    print(chr(i), end="")"""
'''def replaement():'''
for i in range(122, 96,-1):
    char = chr(i) if i % 2 == 0 else chr(i -32)
    print(char, end="")
