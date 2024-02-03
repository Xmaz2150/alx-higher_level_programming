#!/usr/bin/python3
"""Defines a name-printing function"""

def say_my_name(first_name, last_name= ""):
    """
    Prints the provided first and last name, introducing it as "My name is".

    Args:
        first_name (str): The first name to print.
        last_name (str, optional): The last name to print. Defaults to "".

    Raises:
        TypeError: If either first_name or last_name is not a string.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
