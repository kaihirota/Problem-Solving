"""
Restaurant
https://www.hackerrank.com/challenges/restaurant/problem
"""

import os
import sys
from math import gcd
#
# Complete the restaurant function below.
#
def restaurant(l, b):
    denom = gcd(l, b)
    return int((l / denom) * (b / denom))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        lb = input().split()

        l = int(lb[0])

        b = int(lb[1])

        result = restaurant(l, b)

        fptr.write(str(result) + '\n')

    fptr.close()
