#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    ans = 1
    f = lambda x: sum(map(int, list(str(x))))

    if n == 1:
        print(1)
    else:
        for i in range(n, 1, -1):
            # print(i, f(i))
            if n % i == 0:
                if f(i) > f(ans):
                    ans = i
                elif f(i) == f(ans) and i < ans:
                    ans = i

        print(ans)
