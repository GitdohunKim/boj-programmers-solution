import sys
input = sys.stdin.readline

max_depth = 40000
LOG = 0
while True:
    if 2 ** LOG > max_depth:
        LOG += 1
        break
    LOG += 1

n = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, distance = map(int, input().split())
    graph[a].append([b, distance])
    graph[b].append([a, distance])

tree = [[[0, 0] for _ in range(LOG)] for _ in range(n+1)]

visit = [1]
level = [-1 for _ in range(n+1)]
level[1] = 0

while visit:
    now = visit.pop()

    for next_node, distance in graph[now]:
        if level[next_node] != -1:
            continue

        level[next_node] = level[now] + 1
        tree[next_node][0][0] = now
        tree[next_node][0][1] = distance
        visit.append(next_node)

for i in range(1, LOG):
    for j in range(1, n+1):
        parent = tree[tree[j][i - 1][0]][i - 1][0]
        dis_ = tree[j][i-1][1] + tree[tree[j][i - 1][0]][i - 1][1]
        tree[j][i] = [parent, dis_]

m = int(input())

for _ in range(m):
    a, b = map(int, input().split())

    distance = 0

    if level[a] < level[b]:
        a, b = b, a

    for i in range(LOG-1, -1, -1):
        if level[a] - level[b] >= 2 ** i:
            distance += tree[a][i][1]
            a = tree[a][i][0]

    if a == b:
        print(distance)
        continue

    for i in range(LOG-1, -1, -1):
        if tree[a][i][0] != tree[b][i][0]:
            distance += tree[a][i][1]
            distance += tree[b][i][1]
            a = tree[a][i][0]
            b = tree[b][i][0]

    distance += tree[a][0][1]
    distance += tree[b][0][1]

    print(distance)
