import heapq as hq
import sys

inf = 1e9

def dijkstra(start, end, graph, edges):
    visit = [inf] * n
    visit[start] = 0
    trace = [[] for _ in range(n)]
    heap = [(0, start)]

    while heap:
        c, x = hq.heappop(heap)

        for nx in graph[x]:
            if (x, nx) not in shortcut:
                nc = c + edges[x][nx]

                if nc < visit[nx]:
                    visit[nx] = nc
                    trace[nx] = [x]
                    if nx != end:
                        hq.heappush(heap, (nc, nx))
                elif nc == visit[nx]:
                    trace[nx].append(x)

    return visit, trace

def dfs(x):
    global T, shortcut, start, D

    if D[x] or x == start:
        return

    D[x] = True

    for px in T[x]:
        shortcut.add((px, x))
        dfs(px)

while True:
    n, m = map(int, sys.stdin.readline().split())

    if (n, m) == (0, 0):
        break

    start, end = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n)]
    edges = [[inf] * n for _ in range(n)]
    shortcut = set()

    for _ in range(m):
        x, nx, cost = map(int, sys.stdin.readline().split())
        graph[x].append(nx)
        edges[x][nx] = cost

    V, T = dijkstra(start, end, graph, edges)

    if not V[end]:
        print(-1)
    else:
        D = [False] * n
        dfs(end)
        V, T = dijkstra(start, end, graph, edges)

        if V[end] == inf:
            print(-1)
        else:
            print(V[end])
