#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    ac = len(argv)
    myAc = ac - 1

    if ac == 1:
        print("{} arguments.".format(myAc))
    elif ac == 2:
        print("{} argument:".format(myAc))
        print("{}: {}".format((myAc), argv[1]))
    else:
        print("{} arguments:".format(myAc))
        for i in range(1, ac):
            print("{}: {}".format(i, argv[i]))
