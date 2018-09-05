# https://www.hackerrank.com/challenges/sock-merchant/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    type_color = set(ar)
    found = [is_match(ar, color) for color in type_color if is_match(ar, color) > 0 ]
    return sum(found)


def is_match(ar, color):
    return ar.count(color) // 2

if __name__ == '__main__':

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)
