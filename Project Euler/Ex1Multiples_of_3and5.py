
# https://www.hackerrank.com/contests/projecteuler/challenges/euler001
#!/bin/python3

import sys



def sum_dividely(n):
    a = (n - 1) // 3
    b = (n - 1) // 5
    c = (n - 1) // 15
    return 3 * a * (a + 1)//2 + 5 * b * (b + 1)//2 - 15 * c * (c + 1)//2

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(sum_dividely(n))
