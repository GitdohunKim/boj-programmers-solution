import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(here):
    visited[here] = True
    for there in graph[here]:
        if not visited[there]:
            dfs(there)
    queue.append(here)

def reverse_dfs(here):
    visited[here] = True
    ids[here] = idx
    for there in reverse_graph[here]:
        if not visited[there]:
            reverse_dfs(there)

N, M = map(int, input().split())
graph = [[] for _ in range(N * 2 + 1)]
reverse_graph = [[] for _ in range(N * 2 + 1)]

for _ in range(M):
    i, j = map(int, input().split())
    graph[-i].append(j)
    reverse_graph[j].append(-i)
    graph[-j].append(i)
    reverse_graph[i].append(-j)

queue = []
visited = [False] * (N * 2 + 1)
for here in range(1, N * 2 + 1):
    if not visited[here]:
        dfs(here)

visited = [False] * (N * 2 + 1)
ids = [-1] * (N * 2 + 1)
idx = 0
while queue:
    here = queue.pop()
    if not visited[here]:
        reverse_dfs(here)
        idx += 1

for i in range(1, N + 1):
    if ids[i] == ids[-i]:
        print(0)
        break
else:
    print(1)
