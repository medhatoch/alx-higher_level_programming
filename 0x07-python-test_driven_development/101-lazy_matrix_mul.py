#!/usr/bin/python3
"""
This module defines the lazy_matrix_mul function.

It performs matrix multiplication of two matrices using NumPy.

"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Performs matrix multiplication of two matrices using NumPy.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        numpy.ndarray: The result of the matrix multiplication as a NumPy array.

    Raises:
        ValueError: If m_a or m_b is empty or cannot be multiplied.

    """
    if not m_a or not m_b:
        raise ValueError("m_a can't be empty and m_b can't be empty")

    try:
        result = np.dot(np.array(m_a), np.array(m_b))
        return result.tolist()
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/101-lazy_matrix_mul.txt")
