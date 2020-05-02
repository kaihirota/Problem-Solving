#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxScore' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER m
#

modulo = 10 ** 9 + 7

def maxScore(a, m):
    a = sorted(a)
    total = 0

    counter = 0
    groups = 1
    remainder = len(a) % m

    for i in range(len(a) - remainder):
        if counter == m:
            counter = 0
            groups += 1

        total += groups * a[i]
        counter += 1

    if remainder > 0:
        for j in range(i+1, len(a)):
            total += groups * a[j]

    return total % modulo



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    ans = maxScore(a, m)

    fptr.write(str(ans) + '\n')

    fptr.close()
