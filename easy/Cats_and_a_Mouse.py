# https://www.hackerrank.com/challenges/cats-and-a-mouse/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    distance_A, distance_B = distance_to_C(x, z), distance_to_C(y, z)
    if distance_A == distance_B:
        return "Mouse C"
    return "Cat A" if distance_A < distance_B else "Cat B"

def distance_to_C(cat, mouse):
    return mouse - cat if cat < mouse else cat - mouse


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()

