# https://www.hackerrank.com/challenges/day-of-the-programmer/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    if year == 1918:
        return '26.09.1918'
    return "12.09.{}".format(year) if is_leap_year(year) else "13.09.{}".format(year)

def is_leap_year(year):
    if year <= 1919:
        return year % 4 == 0
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 


if __name__ == '__main__':
    
    year = int(input().strip())

    result = dayOfProgrammer(year)

    print(result)
