#!/bin/python3
# https://www.hackerrank.com/challenges/angry-professor/problem
import math
import os
import random
import re
import sys

# Complete the angryProfessor function below.
def angryProfessor(k, a):
    found = 0
    for student in a:
        found += 1 if student <= 0 else 0
    return "YES" if found < k else "NO"

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        print(result)
