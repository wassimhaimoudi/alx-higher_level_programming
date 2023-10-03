#!/usr/bin/python3
def uppercase(str):
    for c in str:
        order = ord(c)
        if order >= 97 and order <= 122:
            order -= 32
        print('{}'.format(chr(ordert)), end='')
    print()
