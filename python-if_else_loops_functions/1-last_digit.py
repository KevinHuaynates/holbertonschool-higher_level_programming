#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
def lastnum(number):
    return number % 10
if lastnum(number) > 5:
    print(f"Last digit of {number} is {lastnum(number)} and is greater than 5")
elif lastnum(number) == 0:
    print(f"last digit of {number} is {lastnum(number)} and is 0")
elif lastnum(number) < 6 and lastnum(number) != 0:
    print(f"Last digit of {number} is {lastnum(number)} and is less than 6 and not 0")
