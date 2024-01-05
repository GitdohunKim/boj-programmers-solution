import sys
import heapq

input = sys.stdin.readline
n, k = map(int, input().split())
items = []
bag = []
candi = []
answer = 0
for _ in range(n):
    heapq.heappush(items, list(map(int, input().split())))
for _ in range(k):
    bag.append(int(input()))
bag = sorted(bag)

for cap in bag:
    while items and items[0][0] <= cap:
        heapq.heappush(candi, -heapq.heappop(items)[1])
    if candi:
        answer += abs(heapq.heappop(candi))
print(answer)