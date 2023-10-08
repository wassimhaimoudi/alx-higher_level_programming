#!/usr/bin/pyhton3
def print_list_integer(my_list=[]):
    for integer in my_list:
        print('{:d}'.format(integer))


if __name__ == '__main__':
    mylist = [1, 4, 0, -1]
    print_list_integer(mylist)
