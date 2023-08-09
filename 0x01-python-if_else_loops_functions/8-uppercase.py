#!/usr/bin/python3
def uppercase(str):
    for char in str:
        ascii_value = ord(char)
        if ascii_value >= 97 and ascii_value <= 122:
            print("{:c}".format(ascii_value - 32), end="")
        else:
            print("{:c}".format(ascii_value), end="")
    print()
