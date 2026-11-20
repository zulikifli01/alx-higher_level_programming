#!/usr/bin/python3
'''a_list = [1, 2, 3, 4, 5]

def replace_values(list_to_replace, item_to_replace, item_to_replace_with):
    return [item_to_replace_with if item == item_to_replace else item for item in list_to_replace]

replaced_list = replace_values(a_list, 4, 9)
print(replaced_list)
print(replaced_list)'''

'''orig = [1, 2, 3, 4, 5]
toFind = 4
replacement = 9
def findAndReplace(orig, toFind, replacement):
    for i, element in enumerate(orig):
        if element == toFind:
            orig[i] = replacement
    return orig
print(findAndReplace(orig, toFind, replacement))'''

def replace_in_list(my_list, idx, element):
    for i, num in enumerate(my_list):
        if num == idx:
            my_list[i] = new_element
    return my_list
