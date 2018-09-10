# # https://www.hackerrank.com/contests/projecteuler/challenges/euler006/problem
# 1) sum of first n natural numbers is = n*(n+1)/2

# 2) sum of first n natural numbers idiviual squares is : : n*(n+1)*(2*n+1)/6 

#!/bin/python3

import sys

def difference(n):
    return (n*(n+1)//2)**2 - n*(n+1)*(2*n+1)//6

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(difference(n))