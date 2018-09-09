# https://www.hackerrank.com/contests/projecteuler/challenges/euler005
#!/bin/python3

import sys

def dividely(n, number):
    if n == 1:
        return True
    return dividely(n-1, number) if number % n == 0 else False

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    i = 1
    while dividely(n, i) is False:
        i += 1
    print(i)
