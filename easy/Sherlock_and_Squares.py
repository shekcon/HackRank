#!/bin/python3
# https://www.hackerrank.com/challenges/sherlock-and-squares/problem
import math
import os
import random
import re
import sys

# Complete the squares function below.
def pow_numbers():
    i = 1
    numbers = []
    while i**2 <= 10**9:
        numbers.append(i**2)
        i += 1 
    return numbers

array_square = pow_numbers()
# base on binary search algorithms
def search_index(num, check, mode):
    global array_square
    first = 0
    last = len(array_square) - 1
    while first<=last:
        midpoint = (first + last)//2
        if array_square[midpoint] == num:
            return midpoint
        else:
            if num < array_square[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    try:
        if mode == "start":
            if num <= array_square[midpoint] and check >= array_square[midpoint]:
                return midpoint
            elif num > array_square[midpoint] and check >= array_square[midpoint+1]:
                return midpoint + 1
            return -1
        if num >= array_square[midpoint] and check <= array_square[midpoint]:
            return midpoint
        return midpoint - 1 if num < array_square[midpoint] and check <= array_square[midpoint - 1] else -1
    except BaseException:
        return -1
        

def squares(a, b):
    """ solution one"""
    # loc_a = search_index(a, b, "start")
    # loc_b = search_index(b, a, "end")
    # return 0 if loc_a == -1 or loc_b == -1 else loc_b - loc_a + 1
    """solution two"""
    loc_a = int(math.sqrt(a))
    loc_b = int(math.sqrt(b))
    print(loc_a,loc_b)
    return loc_b - loc_a +1 if loc_a ** 2 == a else loc_b - loc_a

    


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        print(str(result))

