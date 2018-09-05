
# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
# !/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    highest_score = scores[0]
    lowest_score = scores[0]
    del scores[0]
    break_high = 0
    break_low = 0
    for score in scores:
        break_high += 1 if break_record(score, highest_score) else 0
        break_low += 1 if break_record(lowest_score, score) else 0
        highest_score = max(highest_score, score)
        lowest_score = min(lowest_score, score)
    return [break_high,break_low]

def break_record(first, second):
    """first is greater than second or not"""
    return first > second

if __name__ == '__main__':

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(' '.join(map(str, result)))