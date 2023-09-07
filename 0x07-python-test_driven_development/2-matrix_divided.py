#!/usr/bin/python3
"""
This module defines the matrix_divided function.

It divides all elements of a matrix by a specified number and returns a new matrix.

"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a specified number and returns a new matrix.

    Args:
        matrix (list of lists): The input matrix of integers or floats.
        div (int or float): The divisor.

    Returns:
        list of lists: A new matrix where all elements are divided by div and rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats, or if div is not a number (int or float).
        ZeroDivisionError: If div is equal to 0.
        TypeError: If rows of the matrix have different sizes.

    """
    # Check if matrix is a list of lists and div is a number (int or float)
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix) or not all(isinstance(val, (int, float)) for row in matrix for val in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Check if all rows have the same size
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    
    # Perform the division and round to 2 decimal places
    new_matrix = [[round(val / div, 2) for val in row] for row in matrix]
    
    return new_matrix

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
