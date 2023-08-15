#!/usr/bin/python3
"""
Module containing the divisible_by_2 function.
"""

def divisible_by_2(my_list=[]):
    """
    Finds all multiples of 2 in a list.
    Args:
        my_list (list): The list of integers.
    Returns:
        A new list with True or False, depending on whether each integer in the original list is a multiple of 2.
    """
    result_list = [num % 2 == 0 for num in my_list]
    return result_list

if __name__ == "__main__":
    my_list = [0, 1, 2, 3, 4, 5, 6]
    list_result = divisible_by_2(my_list)

    i = 0
    while i < len(list_result):
        print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
        i += 1
