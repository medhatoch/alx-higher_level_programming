#!/usr/bin/python3
"""
Module containing the replace_in_list function.
"""

def replace_in_list(my_list, idx, element):
    """
    Replaces an element of a list at a specific position.
    Args:
        my_list (list): The list in which to replace the element.
        idx (int): The index at which to replace the element.
        element: The new element to replace the existing element.
    Returns:
        The modified list if the index is valid, or the original list if idx is negative or out of range.
    """
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
    return my_list

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_element = 9
    new_list = replace_in_list(my_list, idx, new_element)

    print(new_list)
    print(my_list)
