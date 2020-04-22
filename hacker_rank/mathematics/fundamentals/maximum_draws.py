"""
Maximum Draws
https://www.hackerrank.com/challenges/maximum-draws/problem

Jim is off to a party and is searching for a matching pair of socks. His drawer is filled with socks, each pair of a different color. In its worst case scenario, how many socks (x) should Jim remove from his drawer until he finds a matching pair?

Input Format
The first line contains the number of test cases T.
Next T lines contains an integer N which indicates the total pairs of socks present in the drawer.

Output Format
Print the number of Draws (x) Jim makes in the worst case scenario.

Constraints


Sample Input

2
1
2
Sample Output

2
3
Explanation
Case 1 : A pair of socks are present, hence exactly 2 draws for the socks to match.
Case 2 : 2 pair of socks are present in the drawer. The first and the second draw might result in 2 socks of different color. The 3rd sock picked will definitely match one of previously picked socks. Hence, 3.


"""
#!/bin/python3

import os
import sys

#
# Complete the maximumDraws function below.
#
def maximumDraws(n):
    return ((n * 2) // 2) + 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = maximumDraws(n)

        fptr.write(str(result) + '\n')

    fptr.close()
