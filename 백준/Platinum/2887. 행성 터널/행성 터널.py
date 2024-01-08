from sys import stdin
from heapq import heappop, heapify

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    x, y = find(a), find(b)
    if x != y:
        parent[x] = y

n = int(stdin.readline())
xcoor, ycoor, zcoor = [], [], []
parent = [i for i in range(n)]

for i in range(n):
    x, y, z = map(int, stdin.readline().split())
    xcoor.append((x, i))
    ycoor.append((y, i))
    zcoor.append((z, i))

xcoor.sort()
ycoor.sort()
zcoor.sort()

pq = []

for coords in [xcoor, ycoor, zcoor]:
    for i in range(n - 1):
        coord1, a = coords[i]
        coord2, b = coords[i + 1]
        pq.append((coord2 - coord1, a, b))

heapify(pq)

result = 0

while pq:
    w, a, b = heappop(pq)
    if find(a) != find(b):
        result += w
        union(a, b)

print(result)
