#!/bin/python3
# https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem
import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    sub_energy = [ 3 if c[i] == 1 else 1 for i in range(0, len(c), k) ]
    return 100 - sum(sub_energy)    

if __name__ == '__main__':


    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    print(str(result))

