import sys
from collections import deque

def topological_sort(v, e, edges):
    indegree = [0] * (v + 1)
    graph = [[] for _ in range(v + 1)]

    for edge in edges:
        for i in range(len(edge) - 2):
            graph[edge[i + 1]].append(edge[i + 2])
            indegree[edge[i + 2]] += 1

    result = []
    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    return result

def main():
    input = sys.stdin.readline
    v, e = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(e)]
    result = topological_sort(v, e, edges)

    if len(result) != v:
        print(0)
    else:
        for i in result:
            print(i)

if __name__ == "__main__":
    main()
