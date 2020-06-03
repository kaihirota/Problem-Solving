"""
https://codeforces.com/problemset/problem/727/D

D. T-shirts Distribution

The organizers of a programming contest have decided to present t-shirts to participants. There are six different t-shirts sizes in this problem: S, M, L, XL, XXL, XXXL (sizes are listed in increasing order). The t-shirts are already prepared. For each size from S to XXXL you are given the number of t-shirts of this size.

During the registration, the organizers asked each of the n participants about the t-shirt size he wants. If a participant hesitated between two sizes, he could specify two neighboring sizes — this means that any of these two sizes suits him.

Write a program that will determine whether it is possible to present a t-shirt to each participant of the competition, or not. Of course, each participant should get a t-shirt of proper size:

the size he wanted, if he specified one size;
any of the two neibouring sizes, if he specified two sizes.
If it is possible, the program should find any valid distribution of the t-shirts.

Input
The first line of the input contains six non-negative integers — the number of t-shirts of each size. The numbers are given for the sizes S, M, L, XL, XXL, XXXL, respectively. The total number of t-shirts doesn't exceed 100 000.

The second line contains positive integer n (1 ≤ n ≤ 100 000) — the number of participants.

The following n lines contain the sizes specified by the participants, one line per participant. The i-th line contains information provided by the i-th participant: single size or two sizes separated by comma (without any spaces). If there are two sizes, the sizes are written in increasing order. It is guaranteed that two sizes separated by comma are neighboring.

Output
If it is not possible to present a t-shirt to each participant, print «NO» (without quotes).

Otherwise, print n + 1 lines. In the first line print «YES» (without quotes). In the following n lines print the t-shirt sizes the orginizers should give to participants, one per line. The order of the participants should be the same as in the input.

If there are multiple solutions, print any of them.

Examples

0 1 0 1 1 0
3
XL
S,M
XL,XXL

YES
XL
M
XXL

1 1 2 0 1 1
5
S
M
S,M
XXL,XXXL
XL,XXL

NO

1. s node: 6 edges -> sizes, where capacity is quantity of each size
2. S  M  L XL XXL XXL -> candidates matched by preference, capacity = 1
3. candidates -> t node
"""

from problem_solving.algorithms.ford_fulkerson import Graph
from collections import defaultdict, deque

# S, M, L, XL, XXL, XXXL = map(int, input().strip().split())
sizes = deque(list(map(int, input().strip().split())))
N = int(input())

mapping = {'S': 1, 'M': 2, 'L': 3, 'XL': 4, 'XXL': 5, 'XXXL': 6,
            1: 'S', 2: 'M', 3: 'L', 4: 'XL', 5: 'XXL', 6: 'XXXL'}

size = len(sizes) + N + 2
graph = [[0] * size for _ in range(size)]

for person in range(7, 7 + N):
    for size in input().strip().split(','):
        size = mapping[size]
        graph[size][person] += 1
        graph[person][-1] = 1

sizes.appendleft(0)
for i in range(N + 1):
    sizes.append(0)

graph[0] = list(sizes)

for row in graph:
    print(row)

g = Graph(graph)
source = 0
sink = len(graph) - 1

maxflow = g.FordFulkerson(source, sink)

if maxflow == N:
    print('YES')

    for person in range(7, 7 + N):
        print(mapping[graph[person].index(1)])
else:
    print('NO')

print('residual graph')
for row in graph:
    print(row)
