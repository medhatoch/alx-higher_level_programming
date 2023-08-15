#!/usr/bin/python3
"""
Module containing the max_integer function.
"""

def max_integer(my_list=[]):
    """
    Finds the biggest integer of a list.
    Args:
        my_list (list): The list of integers.
    Returns:
        The largest integer in the list, or None if the list is empty.
    """
    if len(my_list) == 0:
        return None

    max_value = my_list[0]
    for num in my_list:
        if num > max_value:
            max_value = num
    return max_value

if __name__ == "__main__":
    my_list = [1, 90, 2, 13, 34, 5, -13, 3]
    max_value = max_integer(my_list)
    print("Max: {}".format(max_value))
