#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """This class represents a square."""

    def __init__(self, size=0):
        """Initialize the square with the given size."""
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def __lt__(self, other):
        """Less than comparator based on square area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal comparator based on square area."""
        return self.area() <= other.area()

    def __eq__(self, other):
        """Equal comparator based on square area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Not equal comparator based on square area."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Greater than comparator based on square area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal comparator based on square area."""
        return self.area() >= other.area()
