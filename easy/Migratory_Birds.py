# https://www.hackerrank.com/challenges/migratory-birds/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
    def migratoryBirds(arr):
        frequents = [arr.count(type) for type in range(1,6)]
        most_sighting = max(frequents)
        most_type = [type for type in range(1,6) if arr.count(type) == most_sighting]
        return min(most_type)

if __name__ == '__main__':


    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(result)