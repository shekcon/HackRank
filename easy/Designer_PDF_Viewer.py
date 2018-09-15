#!/bin/python3
# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    h_letters = { letter:height for letter, height in zip(letters, h)}
    max_h = max([ h_letters[letter] for letter in word])
    return max_h * len(word)


if __name__ == '__main__':

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    print(str(result))

