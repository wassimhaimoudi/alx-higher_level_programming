#!/usr/bin/python3
def max_integer(my_list):
    if my_list:
        my_list.sort()
        biggest = my_list[-1]
        return (biggest)
