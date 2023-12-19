#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        new_list = []
        for i in range(list_length):
            n1 = my_list_1[i]
            n2 = my_list_2[i]

            if not (isinstance(n1, int) and isinstance(n2, int)):
                print("wrong type")
                new_list.append(0)
                continue
            if n1 > 0 and n2 == 0:
                print("division by 0")
                new_list.append(0)
            else:
                new_list.append(n1/n2)
        return new_list
    except IndexError:
        print("out of range")
        if len(new_list) < list_length:
            new_list.append(0)
        return new_list
