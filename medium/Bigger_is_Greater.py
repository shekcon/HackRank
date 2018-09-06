# https://www.hackerrank.com/challenges/bigger-is-greater/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    for i in range(len(w)-2, -1, -1):
        old_text = "".join(w[i:])
        head_new_text = get_first_new_text(old_text) 
        new_text = head_new_text + get_body_new_text(head_new_text, old_text)
        if new_text > old_text:
            return head(i,w) + new_text
    return "no answer"

def get_first_new_text(oldtext):
    bigger_letter = [ letter for letter in oldtext[1:] if letter > oldtext[0]]
    return str(min(bigger_letter)) if len(bigger_letter) > 0 else oldtext[0]

def get_body_new_text(head, oldtext):
    body = [letter for letter in oldtext if letter != head]
    return smallest_new_text(body)

def head(i, w):
    return "".join(w[:i])


def smallest_new_text(text):
    return "".join(sorted(text[:], key=str))

if __name__ == '__main__':

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        print(result)
