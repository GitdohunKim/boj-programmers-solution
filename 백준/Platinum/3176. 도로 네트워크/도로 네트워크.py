import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    edge = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a, b, c = map(int, input().split())
        edge[a].append((b, c))
        edge[b].append((a, c))
    depth = [-1] * (n+1)
    distance = [[[int(1e6), 0] for __ in range(n+1)] for _ in range(17)]
    parent = [[0] * (n+1) for _ in range(17)]
    stack = [(1, 0)]
    while stack:
        cur, dep = stack.pop()
        depth[cur] = dep
        for nx, dist in edge[cur]:
            if depth[nx] == -1:
                parent[0][nx] = cur
                distance[0][nx] = [dist, dist]
                stack.append((nx, dep+1))
    for i in range(1, 17):
        for j in range(1, n+1):
            parent[i][j] = parent[i-1][parent[i-1][j]]
            distance[i][j][0] = min(distance[i-1][parent[i-1][j]][0], distance[i-1][j][0])
            distance[i][j][1] = max(distance[i-1][parent[i-1][j]][1], distance[i-1][j][1])
    k = int(input())
    for _ in range(k):
        d, e = map(int, input().split())
        if depth[d] > depth[e]:
            d, e = e, d
        min_dist, max_dist = int(1e6), 0
        for i in range(16, -1, -1):
            if depth[e] - depth[d] >= (1 << i):
                min_dist = min(min_dist, distance[i][e][0])
                max_dist = max(max_dist, distance[i][e][1])
                e = parent[i][e]
        if d == e:
            print(min_dist, max_dist)
            continue
        for i in range(16, -1, -1):
            if parent[i][d] != parent[i][e]:
                min_dist = min(min_dist, distance[i][d][0], distance[i][e][0])
                max_dist = max(max_dist, distance[i][d][1], distance[i][e][1])
                d = parent[i][d]
                e = parent[i][e]
        print(min(min_dist, distance[0][d][0], distance[0][e][0]), max(max_dist, distance[0][d][1], distance[0][e][1]))

solve()
