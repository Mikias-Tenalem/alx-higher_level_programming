#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_str = ''
if int(str(number)[-1]) > 5:
    last_str = 'and is greater than 5'
elif int(str(number)[-1]) == 0:
    last_str = 'and is 0'
elif int(str(number)[-1]) < 6 & int(str(number)[-1]) != 0:
    last_str = 'and is less than 6 and not 0'
print(f"Last digit of {number} is {str(number)[-1]} {last_str}")
