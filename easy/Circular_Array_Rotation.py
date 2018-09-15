#!/bin/python3
# https://www.hackerrank.com/challenges/circular-array-rotation/problem
import math
import os
import random
import re
import sys

# Complete the circularArrayRotation function below.
def circularArrayRotation(n, a, k, queries):
    k = k % n
    a = a[-1*k:] + a[:n-k]
    return [a[querie] for querie in queries]

if __name__ == '__main__':

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(n, a, k, queries)

    print('\n'.join(map(str, result)))

