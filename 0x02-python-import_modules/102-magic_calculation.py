#!/usr/bin/python3
def magic_calculation(a, b):
    def add(x, y):
        return (x + y)

    def sub(x, y):
        return (x - y)

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return (c)
    return (sub(a, b))
