#!/usr/bin/python3
"""
Module containing the element_at function.
"""

def element_at(my_list, idx):
    """
    Retrieves an element from a list at a given index.
    Args:
        my_list (list): The list from which to retrieve the element.
        idx (int): The index of the element to retrieve.
    Returns:
        The element at the specified index, or None if idx is out of range or negative.
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
