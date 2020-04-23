#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    t = int(input())

    for test in range(t):
        n, k = list(map(int, input().strip().split()))
        arr = list(range(n-1, -1, -1))

        for i in range(1, n):
            arr[i:] = arr[::-1][:i*-1]

        print(arr.index(k))
