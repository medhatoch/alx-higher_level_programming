#!/usr/bin/python3
"""
Module containing the print_matrix_integer function.
"""

def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers.
    Args:
        matrix (list): The matrix of integers to print.
    """
    for row in matrix:
        for col_idx, num in enumerate(row):
            print("{:d}".format(num), end="")
            if col_idx < len(row) - 1:
                print(" ", end="")
        print()

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print_matrix_integer(matrix)
    print("--")
    print_matrix_integer()
