#!/bin/python3
# https://www.hackerrank.com/challenges/utopian-tree/problem

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    growth = 0
    for i in range(n + 1):
        growth = growth+1 if i % 2 == 0 else growth * 2
    return growth


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        result = utopianTree(n)
        print(result)

