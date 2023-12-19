#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        printed = 0
        for i in range(x):
            try:
                n = int(my_list[i]) 
                print("{:d}".format(n), end="")
                printed += 1
            except (ValueError, TypeError):
                continue
        print()
        return printed
    except IndexError:
        print()
        return printed
