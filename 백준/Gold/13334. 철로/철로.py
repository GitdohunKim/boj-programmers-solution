from sys import stdin
import heapq

n = int(stdin.readline())
roads, data = [], []

for _ in range(n):
    data.append(sorted(list(map(int, stdin.readline().split()))))
train_road_length = int(stdin.readline())


for road in data:
    s, e = road
    if (e - s) <= train_road_length:
        roads.append(road)

roads.sort(key=lambda x: x[1])

answer = 0
q = []

for road in roads:
    if not q:
        heapq.heappush(q, road)
    else:
        while q[0][0] < road[1] - train_road_length:
            heapq.heappop(q)
            if not q:
                break

        heapq.heappush(q, road)
    answer = max(answer, len(q))

print(answer)