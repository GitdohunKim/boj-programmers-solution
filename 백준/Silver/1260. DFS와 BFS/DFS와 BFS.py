from collections import deque
def dfs(graph, v, visted):
    visted[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visted[i]:
            dfs(graph, i, visted)

def bfs(graph, v, visted):
    queue = deque()
    queue.append(v)
    visted[v] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visted[i]:
                queue.append(i)
                visted[i] = True

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
for i in range(N+1):
    graph[i].sort()

visted = [False] * (N+1)
dfs(graph, V, visted)
visted = [False] * (N+1)
print()
bfs(graph, V, visted)