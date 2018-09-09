# https://www.hackerrank.com/contests/projecteuler/challenges/euler008
#!/bin/python3

import sys


def greatest_product(num, n, k):
    digits = [num[i:i+k] for i in range(n-k+1)]
    products =[ product(digit) for digit in digits]
    return max(products)

def product(digit):
    total = 1
    for number in digit:
        total *= int(number)
    return total

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    print(greatest_product(num, n, k))
