# https://www.hackerrank.com/challenges/queens-attack-2/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.

# def validate(loc, obts, n):
#     if loc[0] > n or loc[0] <= 0 or loc[1] > n or loc[1] <= 0:
#         return False
#     for r, c in obts:
#         if r == loc[0] and loc[1] == c:
#             return False
#     return True

# def queensAttack(n, k, r_q, c_q, obstacles):
#     dirs = ([-1, 0],
#             [1, -1],
#             [1, 0],
#             [1, 1],
#             [0, 1],
#             [-1, 1],
#             [0, -1],
#             [-1, -1]
#             )
#     step = 0
#     for direct in dirs:
#         base = [r_q + direct[0], c_q + direct[1]]
#         while validate(base, obstacles, n):
#             base = [base[0] + direct[0], base[1] + direct[1]]
#             step += 1
#     return step


def validate(loc, obts, n):
    if loc[0] > n or loc[0] <= 0 or loc[1] > n or loc[1] <= 0:
        return False
    for r, c in obts:
        if r == loc[0] and loc[1] == c:
            return False
    return True


def queensAttack(n, k, r_q, c_q, obstacles):
    mid = n//2 if n//2 % 2 == 0 else n//2+1
    maxs = [[n, 1],
            [n, mid],
            [n, n],
            [mid, n],
            [1, n],
            [1, mid],
            [1, 1],
            [mid, 1]
    ]
    dirs = [[-1, 0],
            [1, -1],
            [1, 0],
            [1, 1],
            [0, 1],
            [-1, 1],
            [0, -1],
            [-1, -1]]
    for e in object:
        new = tuple(e[0] - r_q, e[1] - c_q)
        for i, di in enumerate(dirs,0):
            if new == tuple(di):
                if tuple(di) == (-1, 0) and di[0] < e[0]: // x
                    maxs[i] = [e[0], e[1]]
                if tuple(di) == (1, -1) and di[0] < e[0]: 
                    maxs[i] = [e[0], e[1]]
                if tuple(di) == (1, 0) and di[0] < e[0]:
                    maxs[i] = [e[0], e[1]]
                if tuple(di) == (1, 1) and di[0] < e[0]:
                    maxs[i] = [e[0], e[1]]
                if tuple(di) == (0, 1) and di[0] < e[0]:
                    maxs[i] = [e[0], e[1]]
                if tuple(di) == (-1, 1) and di[0] < e[0]:
                    maxs[i] = [e[0], e[1]]
                if tuple(di) == (0, -1) and di[0] < e[0]:
                    maxs[i] = [e[0], e[1]]
                if tuple(di) == (-1, -1) and di[0] < e[0]: // x
                    maxs[i] = [e[0], e[1]]
    step=0
    for direct in dirs:
        base=[r_q + direct[0], c_q + direct[1]]
        while validate(base, obstacles, n):
            base=[base[0] + direct[0], base[1] + direct[1]]
            step += 1
    return step


if __name__ == '__main__':
    fptr=open(os.environ['OUTPUT_PATH'], 'w')

    nk=input().split()

    n=int(nk[0])

    k=int(nk[1])

    r_qC_q=input().split()

    r_q=int(r_qC_q[0])

    c_q=int(r_qC_q[1])

    obstacles=[]

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result=queensAttack(n, k, r_q, c_q, obstacles)
    fptr.write(str(result) + '\n')

    fptr.close()
