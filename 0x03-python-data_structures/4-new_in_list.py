#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_copy = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return (list_copy)
    list_copy.pop(idx)
    list_copy.insert(idx, element)
    return (list_copy)
