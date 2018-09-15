#!/bin/python3
# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem 
import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    found = 0
    for i in range(i,j+1):
        found += 1 if is_beau(i, k) else 0
    return found

def is_beau(day, k):
    return abs( day - int(str(day)[::-1])) % k == 0


if __name__ == '__main__':

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    print(result)
