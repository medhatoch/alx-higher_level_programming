#!/usr/bin/python3
"""
Module containing the add_tuple function.
"""

def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds two tuples and returns a new tuple.
    Args:
        tuple_a (tuple): The first tuple.
        tuple_b (tuple): The second tuple.
    Returns:
        A tuple containing the sum of the corresponding elements from tuple_a and tuple_b.
    """
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    sum_tuple = (a[0] + b[0], a[1] + b[1])
    return sum_tuple

if __name__ == "__main__":
    tuple_a = (1, 89)
    tuple_b = (88, 11)
    new_tuple = add_tuple(tuple_a, tuple_b)
    print(new_tuple)

    print(add_tuple(tuple_a, (1,)))
    print(add_tuple(tuple_a, ()))
