#!/bin/python3
# https://www.hackerrank.com/challenges/find-digits/problem
import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    numbers = str(n)
    map_numbers = { int(num):numbers.count(num) for num in set(numbers)}
    divisor_total = 0
    for num in map_numbers.keys():
        divisor_total += map_numbers[num] if num != 0 and n % num == 0 else 0
    return divisor_total
    
    

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        print(str(result))
