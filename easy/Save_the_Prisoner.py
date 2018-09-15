#!/bin/python3
# https://www.hackerrank.com/challenges/save-the-prisoner/problem
import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    m = m % n
    pos =( s + m -1 ) % n
    warn = pos if pos != 0 else n
    return warn

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        print(result)
