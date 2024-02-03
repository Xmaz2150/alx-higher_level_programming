#!/usr/bin/python3
"""Defines a square-printing function"""


def print_square(size):
    """
    Prints a square of # characters to the console,
    with dimensions specified by size.
    Args:
        size: The desired height and width of the square.
        Must be a non-negative integer.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is negative.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)  # Concisely print a row of # characters
