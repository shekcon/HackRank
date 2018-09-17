#!/bin/python3
# https://www.hackerrank.com/challenges/permutation-equation/problem

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(n, p):
    # map location of number
    pos_num = { p[index-1]:index for index in range(1, n+1) }
    # find index of this location for map, at index equal number key
    return [ p.index(pos_num[i])+1 for i in range(1, n+1)]


if __name__ == '__main__':

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(n, p)

    print('\n'.join(map(str, result)))


