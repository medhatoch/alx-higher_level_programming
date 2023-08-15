#!/usr/bin/python3
"""
Module containing the delete_at function.
"""

def delete_at(my_list=[], idx=0):
    """
    Deletes the item at a specific position in a list.
    Args:
        my_list (list): The list of integers.
        idx (int): The index at which to delete the item.
    Returns:
        A new list with the item deleted at the specified index, or the same list if idx is negative or out of range.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list[:]
    
    new_list = [item for i, item in enumerate(my_list) if i != idx]
    return new_list

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_list = delete_at(my_list, idx)
    print(new_list)
    print(my_list)
