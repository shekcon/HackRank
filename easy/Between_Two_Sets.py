# https://www.hackerrank.com/challenges/between-two-sets/problem

#!/bin/python3

import os
import sys

#
# Complete the getTotalX function below.
#


def getTotalX(a, b):
    #
    # Write your code here.
    #
    factors = get_factor(a[-1], b[0], a)
    print(factors)
    i = 0
    while i < len(factors):
        if not validate_factor(factors[i], b, is_factor):
            factors.remove(factors[i])
        else:
            i += 1
    return len(factors)


def get_factor(a, min_b, s):
    factors = []
    number = a
    while number <= min_b:
        if validate_factor(number, s, all_factor):
            factors.append(number)
        number += 1
    return factors


def all_factor(number, n):
    return number % n != 0


def is_factor(number, n):
    return n % number != 0


def validate_factor(number, s, fn):
    for e in s:
        if fn(number, e):
            return False
    return True


if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    print(total)
