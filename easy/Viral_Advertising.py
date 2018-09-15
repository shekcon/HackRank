#!/bin/python3
# https://www.hackerrank.com/challenges/strange-advertising/problem
import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    liked = 2
    shared = 5
    cumalative = 2
    for i in range(2, n+1):
        shared = shared // 2 * 3
        liked = shared // 2
        cumalative += liked  
    return cumalative

if __name__ == '__main__':

    n = int(input())

    result = viralAdvertising(n)

    print(result)


