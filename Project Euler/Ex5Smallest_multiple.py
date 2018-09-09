# https://www.hackerrank.com/contests/projecteuler/challenges/euler005
#!/bin/python3

import sys

def dividely(n, number):
    if n == 1:
        return True
    return dividely(n-1, number) if number % n == 0 else False

"""
 from functools import reduce
 from fractions import gcd

 def lcm(a, b):
     return a * b / gcd(a, b)

 def lcms(*numbers):
      return reduce(lcm, numbers)

 def gcds(*numbers):
      return reduce(gcd, numbers)
"""

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    i = 1
    while dividely(n, i) is False:
        i += 1
    print(i)
    """can use this way
    print(reduce(lcm,[number for number in range(1, n+1)]))

    """
