# https://www.hackerrank.com/challenges/manasa-and-stones/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# 10 10 10 10
# 10 10 10 100
# 10 10 100 100
# 10 100 100 100
# 10 100 10 10
# 10 10 100 10
# 10 100 100 10
# 10 100 10 100

# Complete the stones function below.
def stones(n, a, b):
    pass
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        n = int(input())

        a = int(input())

        b = int(input())

        result = stones(n, a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

