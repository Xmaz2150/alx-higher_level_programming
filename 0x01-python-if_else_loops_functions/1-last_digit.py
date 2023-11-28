#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDgt = number % 10 if number > 0 else ((number * -1) % 10) * -1

if lastDgt > 5:
    print(f"Last digit of {number} is {lastDgt} and is greater than 5")
elif lastDgt == 0:
    print(f"Last digit of {number} is {lastDgt} and is 0")
elif lastDgt < 6:
    print(f"Last digit of {number} is {lastDgt} and is less than 6 and not 0")
