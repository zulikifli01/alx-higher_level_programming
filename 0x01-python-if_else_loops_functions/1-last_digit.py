#!/bin/env python
import random
number = random.randint(-10000, 10000)
str_number = str(number)
last_digit = int(str_number[-1])
# (f"last digit of {number} is {last_digit}")
if last_digit > 5:
    print(f"last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"last digit of {number} is {last_digit} and is 0")
else:
    print(f"last digit of {number} is {last_digit} and is less than 6 and not 0")
# elif last_digit < 6 and last_digit != 0:
