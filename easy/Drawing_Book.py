# https://www.hackerrank.com/challenges/drawing-book/problem

#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #
    # Write your code here.
    #
    head, end = head_book(n,p), end_book(n, p)
    print(head, end)
    return head if head < end else end

def head_book(n,p):
    found = [ i for i in range(n//2 + 1) if p <= (2*i + 1) ]
    return min(found)

def end_book(n,p):
    found = [ i for i in range(n//2 + 1) if p >= n - 2*i - old_even(n)] 
    return min(found)

def old_even(n):
    return 0 if n % 2 == 0 else 1

if __name__ == '__main__':

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    print(result)
