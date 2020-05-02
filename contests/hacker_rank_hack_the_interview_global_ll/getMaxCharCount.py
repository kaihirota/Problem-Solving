#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMaxCharCount' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. 2D_INTEGER_ARRAY queries
#

from collections import defaultdict
letters = {
    'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g',
    'H': 'h', 'I': 'i', 'J': 'j', 'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n',
    'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's', 'T': 't', 'U': 'u',
    'V': 'v', 'W': 'w', 'X': 'x', 'Y': 'y', 'Z': 'z',
    'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g',
    'h': 'h', 'i': 'i', 'j': 'j', 'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n',
    'o': 'o', 'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't', 'u': 'u',
    'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z'
}

def getMaxCharCount(s, queries):
    s = list(s)
    ret = []

    for a, b in queries:
        counter = defaultdict(int)
        largest = None

        for i in range(a, b+1):
            if largest == None:
                largest = letters[s[i]]
            if letters[s[i]] > largest:
                largest = letters[s[i]]

            counter[letters[s[i]]] += 1

        ret.append(counter[largest])

    return ret


s = 'aAabBcba'
queries = [[2, 6], [1, 2], [2, 2], [0, 4], [0, 7]]
ret = getMaxCharCount(s, queries)
print(ret)
