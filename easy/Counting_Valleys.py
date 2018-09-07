#!/bin/python3
# https://www.hackerrank.com/challenges/counting-valleys/problem
import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    sea_level, found = 0, 0
    for hike in s:
        last_hike = hike
        found += 1 if last_hike == "D" and sea_level == 0 else 0
        sea_level += 1 if hike == "U" else -1  
    return found

if __name__ == '__main__':
    
    n = int(input())
    
    s = input()

    result = countingValleys(n, s)

    print(result)

