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
    climb_record = [ ranked_now(ponit, scores) for ponit in alice]
    return climb_record


def ranked_now(score, leader):
    for rank in range(len(leader)):
        ranked = rank+1 if score >= leader[rank] else None
        if ranked is not None:
            break
    return len(leader)+1 if ranked is None else ranked 



if __name__ == '__main__':

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    print('\n'.join(map(str, result)))


