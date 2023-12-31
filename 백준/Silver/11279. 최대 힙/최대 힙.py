import sys
import heapq
input = sys.stdin.readline

max_heap = []
N = int(input())
for i in range(N):
    temp = int(input())
    if temp: heapq.heappush(max_heap, -temp)
    else:
        if max_heap: print(-heapq.heappop(max_heap))
        else: print(0)