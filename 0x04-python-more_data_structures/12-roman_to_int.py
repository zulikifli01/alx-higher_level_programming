#!/bin/env python
def roman_to_int(roman_string):
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
        'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900
    }

    i = 0
    total = 0

    while i < len(roman_string):
        if i + 1 < len(roman_string) and roman_string[i:i+2] in roman_values:
            total += roman_values[roman_string[i:i+2]]
            i += 2
        else:
            total += roman_values[roman_string[i]]
            i += 1

    return total


print("X =", roman_to_int("X"))
print("VII =", roman_to_int("VII"))
print("IX =", roman_to_int("IX"))
print("LXXXVII =", roman_to_int("LXXXVII"))
print("DCCVIII =", roman_to_int("DCCVII"))
