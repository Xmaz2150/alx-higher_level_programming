#!/usr/bin/python3

def uppercase(str):
    for c in str:
        print("{}".format(c if not islower(c) else chr(ord(c) - 32)), end="")
    print()


def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
