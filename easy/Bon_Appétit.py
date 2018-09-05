# https://www.hackerrank.com/challenges/bon-appetit/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    person_actual = actual_bill(bill, k)
    print("Bon Appetit" if b - person_actual == 0 else b - person_actual)

def actual_bill(bill, k):
    return (sum(bill) - bill[k]) // 2


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
