import heapq
import math


T = int (input())
for t in range(1, T+1):
	n, k = [int(_) for _ in input().split()]
	arr = [int(_) for _ in input().split()]
	res = 0

	heap = []
	for i in range(n - 1):
		heapq.heappush(heap, (-(arr[i+1]-arr[i]), -(arr[i+1]-arr[i]),  1))
	for i in range(k):
		_, num, denum = heapq.heappop(heap)
		denum += 1
		heapq.heappush(heap, (num/denum, num, denum))
	res, num, denum = heapq.heappop(heap)
	res = math.ceil(-res)

	print ("Case #{}: {}".format(t, res))
