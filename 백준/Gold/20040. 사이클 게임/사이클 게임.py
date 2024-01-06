import sys
input = sys.stdin.readline


def find(x):
    path = []
    while head[x] != x:
        path.append(x)
        x = head[x]
    for node in path:
        head[node] = x
    return x


def union(a, b):
    a, b = find(a), find(b)
    head[b] = head[a]


n, m = map(int, input().split())

head = list(range(n))

answer = 0
for i in range(1, m + 1):
    a, b = map(int, input().split())
    if find(a) == find(b):
        answer = i
        break
    union(a, b)

print(answer)
