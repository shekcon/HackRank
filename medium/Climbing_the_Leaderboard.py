#!/bin/python3
# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    scores = list(sorted(set(scores), key=int, reverse=True))
    return [ranked_search(scores, ponit)+1 for ponit in alice]


def ranked_now(score, leader):
    for rank in range(len(leader)):
        ranked = rank+1 if score >= leader[rank] else None
        if ranked is not None:
            break
    return len(leader)+1 if ranked is None else ranked 

# base on binary search algorithms
# solution for exercise on hackrank
def ranked_search(content, score):
    first = 0
    last = len(content) - 1
    # is score bigger than rank 1
    if score >= content[first]:
        return first
    elif score <= content[last]:
        # is item equal lowest ranked or less than
        return last if score == content[last] else last+1
    while first<=last:
        midpoint = (first + last)//2
        if content[midpoint] == score:
            return midpoint
        else:
            if score > content[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    return midpoint if score >= content[midpoint] else midpoint +1

if __name__ == '__main__':

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    print('\n'.join(map(str, result)))


