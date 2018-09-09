# https://www.hackerrank.com/challenges/magic-square-forming/problem
#!/bin/python3

import math
import os
import random
import re
import sys

magic_squares = [
            [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
            ]
# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    global magic_squares
    total = [ cost_total(square, s) for square in magic_squares]
    return min(total)

def cost_total(square, s):
    """find cost for each magic square"""
    cost = [ cost_take(magic, matrix) for magic, matrix in zip(square, s) ]
    return sum(cost)

def cost_take(magic, matrix):
    """ cost for each row magic square"""
    total_col_cost = [ abs(col_magic - col_matrix) for col_magic, col_matrix in zip(magic, matrix)]
    return sum(total_col_cost)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()

