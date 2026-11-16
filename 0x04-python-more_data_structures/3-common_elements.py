#!/bin/env python
def common_elements(set_1, set_2):
    set1 = set(set_1)
    set2 = set(set_2)
    c_set = list(set1.intersection(set2))
    return tuple(sorted(c_set))
