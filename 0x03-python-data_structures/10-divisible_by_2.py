#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        list_result = [x % 2 == 0 for x in my_list]
        return (list_result)
