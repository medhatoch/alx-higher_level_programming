#!/usr/bin/python3
"""
Module containing the no_c function.
"""

def no_c(my_string):
    """
    Removes all characters 'c' and 'C' from a string.
    Args:
        my_string (str): The input string from which to remove 'c' and 'C' characters.
    Returns:
        A new string with 'c' and 'C' characters removed.
    """
    new_string = ''
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char
    return new_string

if __name__ == "__main__":
    print(no_c("Best School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))
