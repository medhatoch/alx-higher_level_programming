#!/usr/bin/python3
"""
Module containing the new_in_list function.
"""

def new_in_list(my_list, idx, element):
    """
    Replaces an element in a list at a specific position without modifying the original list.
    Args:
        my_list (list): The original list.
        idx (int): The index at which to replace the element.
        element: The new element to replace the existing element.
    Returns:
        A new list with the element replaced at the specified index, or the original list if idx is negative or out of range.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list[:]
    new_list = my_list[:]
    new_list[idx] = element
    return new_list

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_element = 9
    new_list = new_in_list(my_list, idx, new_element)

    print(new_list)
    print(my_list)
