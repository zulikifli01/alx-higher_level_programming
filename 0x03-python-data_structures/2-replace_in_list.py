#!/usr/bin/python3

'''a_list = [1, 2, 3, 4, 5]

def replace_values(list_to_replace, item_to_replace, item_to_replace_with):
    return [item_to_replace_with if item == item_to_replace else item for item in list_to_replace]

replaced_list = replace_values(a_list, 4, 9)
print(replaced_list)
print(replaced_list)'''


def replace_in_list(my_list, idx, new_element):
    for i, element in enumerate(my_list):
        if element == 4:
            my_list[i] = new_element
    return my_list


'''def replace_in_list(my_list, idx, element):
    for i, num in enumerate(my_list):
        if num == idx:
            my_list[i] = element
    return my_list'''
