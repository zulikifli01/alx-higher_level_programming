#!/bin/env python
chars = ['a', 'H', 'A', '3', 'g']
for c in chars:
    if c.islower():
        print(f"{c} is lower")
    else:
        print(f"{c} is upper")
