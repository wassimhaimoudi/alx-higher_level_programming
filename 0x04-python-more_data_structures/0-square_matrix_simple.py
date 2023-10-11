#!usr/bin/python3

def square_matrix_simple(matrix=[]):
    sqrt_matrix = [list(map(lambda x: x**2, row)) for row in matrix]
    return sqrt_matrix
