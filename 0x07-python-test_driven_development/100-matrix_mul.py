#!/usr/bin/python3
"""
This module defines the matrix_mul function.

It performs matrix multiplication of two matrices.

"""

def matrix_mul(m_a, m_b):
    """
    Performs matrix multiplication of two matrices.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        list of lists: The result of the matrix multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list of lists, not a rectangle, or contains non-integer/non-float elements.
        ValueError: If m_a or m_b is empty or cannot be multiplied.

    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list and m_b must be a list")
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists and m_b must be a list of lists")
    if not m_a or not m_b:
        raise ValueError("m_a can't be empty and m_b can't be empty")

    # Validate the size and type of elements in m_a and m_b
    for row in m_a:
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError("m_b should contain only integers or floats")

    # Validate the size of the matrices
    size_a = (len(m_a), len(m_a[0]))
    size_b = (len(m_b), len(m_b[0]))

    if size_a[1] != size_b[0]:
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = [[0 for _ in range(size_b[1])] for _ in range(size_a[0])]

    for i in range(size_a[0]):
        for j in range(size_b[1]):
            for k in range(size_b[0]):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
