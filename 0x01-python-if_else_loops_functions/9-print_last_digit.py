#!/usr/bin/python3

def print_last_digit(number):
    if number < 0:
        lastDgt = -(number) % 10
    else:
        lastDgt = number % 10

    print("{}".format(lastDgt), end="")
    return lastDgt
