#!/bin/env python
set_1 = {"Python", "C", "Javascript"}
set_2 = {"Bash", "C", "Ruby", "Perl"}


def only_diff_elements(set_1, set_2):
    set_3 = set_1.symmetric_difference(set_2)
    print(set_3)


only_diff_elements(set_1, set_2)
# set_3 = set_1 ^ set_2
