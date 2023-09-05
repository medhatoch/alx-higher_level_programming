#!/usr/bin/python3

class Rectangle:
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle with optional width and height."""
        self.__width = width  # Private attribute for width
        self.__height = height  # Private attribute for height

    @property
    def width(self):
        """Getter method for retrieving the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for setting the width attribute."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")  # Check for integer type
        elif value < 0:
            raise ValueError("width must be >= 0")  # Check for non-negative value
        self.__width = value  # Set the private width attribute

    @property
    def height(self):
        """Getter method for retrieving the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for setting the height attribute."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")  # Check for integer type
        elif value < 0:
            raise ValueError("height must be >= 0")  # Check for non-negative value
        self.__height = value  # Set the private height attribute

    def area(self):
        """Calculate and return the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
