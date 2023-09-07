#!/usr/bin/python3
"""
This module defines the add_integer function.

It adds two integers and returns the result.

"""

def add_integer(a, b=98):
    """
    Adds two integers and returns the result.

    Args:
        a (int): The first integer.
        b (int, optional): The second integer (default is 98).

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
