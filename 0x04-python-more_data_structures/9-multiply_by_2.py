#!/usr/bin/python3
'''def multiply_by_2(a_dictionary):
    for key in a_dictionary:
        a_dictionary[key] *= 2
    return a_dictionary'''


'''def multiply_by_2(dictionary,x):
    new = {}
    for key in a_dictionary:
        new[key] = a_dictionary[key] * x
    return new
print(multiply_by_2(a_dictionary,x))'''


'''def multiply_by_2(a_dictionary):
    new_list = {key: value * 2 for key, value in a_dictionary.items()}
    print(new_list)'''


'''def multiply_by_2(a_dictionary):
    for key in a_dictionary:
        a_dictionary[key] *= 2'''


def multiply_by_2(a_dictionary):
    return {key: value * 2 for key, value in a_dictionary.items()}
