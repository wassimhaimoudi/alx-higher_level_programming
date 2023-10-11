#!usr/bin/python3


def square_matrix_simple(matrix=[]):
    """
    A function that computes the square
    value of all integers in a matrix
    """
    sqrt_matrix = [list(map(lambda x: x**2, row)) for row in matrix]
    return (sqrt_matrix)
