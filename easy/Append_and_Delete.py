# https://www.hackerrank.com/challenges/append-and-delete/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    """
    return str
    """
    statement = is_same_text(s, t)
    delete, append = delete_append_time_minium(statement, s, t)
    print(delete, append)
    while k - delete - append >= 0:
        if k - delete - append == 0:
            return 'Yes'
        delete += 1
        """only increment when add not greater than len of array"""
        append += 1 if append < len(t) else 0
    return "No"
    

def delete_append_time_minium(flag, s, t):
    """
    cal delete_time_minium and append time minium
    return int, int
    """
    delete_time = len(s) - flag if flag != -1 else len(s)
    append_time = len(t) - flag if flag != -1 else len(t)
    return delete_time, append_time
    

def is_same_text(s, t):
    """
    find s start with equal t
    return int
    """
    found = [i for i in range(1,len(t)+1) if s.startswith("".join(t[:i]))]
    return max(found) if len(found) > 0 else -1


if __name__ == '__main__':
    

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    print(result)
