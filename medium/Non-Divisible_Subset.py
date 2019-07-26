#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#


def getValidate(subset, k):
    check = 1
    i = 2
    while check < len(subset):
        i = 1
        while i < len(subset):
            if (subset[check] + subset[i]) % k == 0 and check != i:
                subset.remove(subset[i])
            else:
                i += 1
        check += 1
        

def nonDivisibleSubset(k, s):
    list_subset = {
        'subsetMax': {
            'index': 0,
            'list_subset': [s[0]]
        },
        'current': {
            'index': 0,
            'list_subset': [s[0]]
        }
    }
    length = len(s)
    track = 1
    try:
        while track < length:
            i = 1
            value = list_subset["current"]["index"]
            while i < length:
                if (s[value] + s[i]) % k != 0 and value != i:
                    list_subset["current"]["list_subset"].append(s[i])
                i += 1
            print("pre:" + str( list_subset["current"]["list_subset"]))
            if len(list_subset["subsetMax"]["list_subset"]) < len(list_subset["current"]["list_subset"]):
                getValidate(list_subset["current"]["list_subset"], k)
                if (len(list_subset["subsetMax"]["list_subset"]) < len(list_subset["current"]["list_subset"])):
                    list_subset["subsetMax"]["list_subset"] = list_subset["current"]["list_subset"]
            list_subset["current"]["list_subset"] = [s[value + 1]]
            list_subset["current"]["index"] = value + 1
            print("validate:" + str( list_subset["subsetMax"]["list_subset"]))
            track += 1
    except IndexError:
        if len(s) == 1:
            return 1
    print(list_subset["subsetMax"]["list_subset"])
    return len(list_subset["subsetMax"]["list_subset"])




if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # first_multiple_input = input().rstrip().split()
    first_multiple_input = "10 5".rstrip().split()
    list_input = "770528134 663501748 384261537 800309024 103668401 538539662 385488901 101262949 557792122 46058493"
    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])
    s = list(map(int, list_input.rstrip().split()))

    result = nonDivisibleSubset(k, s)

    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
