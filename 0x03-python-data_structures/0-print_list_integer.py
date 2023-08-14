#!/usr/bin/python3
"""
Module containing the print_list_integer function.
"""

def print_list_integer(my_list=[]):
    """
    Prints all integers of a list.
    Args:
        my_list (list): The list of integers to print.
    """
    for num in my_list:
        print("{:d}".format(num))

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print_list_integer(my_list)
