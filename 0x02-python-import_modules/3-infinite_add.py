#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    ac = len(argv)
    aSum = 0

    if ac == 1:
        print("0")
    else:
        for i in range(1, ac):
            arg = argv[i]
            aSum += int(arg)
        print("{}".format(aSum))
