# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    found = [[ar[i], number] for i in range(n) for number in ar[i+1:] if check_pair(ar[i], number, k)]
    return len(found)


def check_pair(pair_one, pair_second, match):
    return (pair_one + pair_second) % match == 0


if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    print(result)