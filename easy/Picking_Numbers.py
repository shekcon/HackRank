#!/bin/python3
# https://www.hackerrank.com/challenges/picking-numbers/problem
import math
import os
import random
import re
import sys

# Complete the pickingNumbers function below.
def pickingNumbers(a, n):
    a = sorted(a, key=int)
    numbers = list(set(a))
    max_pick = [ number_chosen(number, a) for number in numbers ] 
    return max(max_pick) if len(max_pick) > 0 else len(a)


def number_chosen(num, a):
    return a.count(num) + a.count(num+1) if num + 1 in a else a.count(num)

if __name__ == '__main__':
    
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a, n)
    
    print(result)
