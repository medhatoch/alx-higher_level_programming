#!/usr/bin/python3

class Rectangle:
    def __init__(self, width=0, height=0):
        """
        Constructor for the Rectangle class.
        Initializes a Rectangle object with width and height.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Getter method for the width property.
        Returns the width of the Rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width property.
        Sets the width of the Rectangle and performs validation.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height property.
        Returns the height of the Rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height property.
        Sets the height of the Rectangle and performs validation.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate and return the area of the Rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate and return the perimeter of the Rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Generate a string representation of the Rectangle.
        Returns a string with '#' characters forming a rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(['#' * self.__width] * self.__height)

    def __repr__(self):
        """
        Generate a string representation of the Rectangle for debugging.
        Returns a string in the format "Rectangle(width, height)".
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
