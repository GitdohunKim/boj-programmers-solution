import sys
import heapq
N = int(sys.stdin.readline().rstrip())
heap=[]
for i in range(N):
    n=int(sys.stdin.readline().rstrip())
    if n!=0:
        heapq.heappush(heap, n)
    else:
        if heap: 
            print(heapq.heappop(heap))
        else: 
            print(0)
