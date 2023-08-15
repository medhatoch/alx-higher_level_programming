#!/usr/bin/python3
"""
Module containing the multiple_returns function.
"""

def multiple_returns(sentence):
    """
    Returns a tuple with the length of a string and its first character.
    Args:
        sentence (str): The input sentence.
    Returns:
        A tuple containing the length of the sentence and its first character.
    """
    length = len(sentence)
    first = None if length == 0 else sentence[0]
    return length, first

if __name__ == "__main__":
    sentence = "At school, I learnt C!"
    length, first = multiple_returns(sentence)
    print("Length: {:d} - First character: {}".format(length, first))
