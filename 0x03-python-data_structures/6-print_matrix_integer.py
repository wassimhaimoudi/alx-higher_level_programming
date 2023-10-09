#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
            for row in matrix:
                for integer in row:
                    print('{:d}'.format(integer), end='')
                    if row.index(integer) < (len(row) - 1):
                        print(' ', end='')
                print()
