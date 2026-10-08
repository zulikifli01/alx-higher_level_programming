#!/bin/env python
def print_last_digit(number):
    last_digit = abs(number) % 10
    print(f"{last_digit}", end="\n")
    return last_digit
print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)
