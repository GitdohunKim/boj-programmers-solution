from sys import stdin

def solution(V, edges):

    answer = 0

    parent = [i for i in range(V+1)]
    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]
    def union(x,y):
        x = find(x)
        y = find(y)
        parent[max(x,y)] = parent[min(x,y)]

    edges.sort(key = lambda x : x[2])

    for s, e, w in edges:
        if find(s) != find(e):
            union(s,e)
            answer += w

    return answer

V, E = map(int,stdin.readline().split())
edges = [list(map(int,stdin.readline().split())) for _ in range(E)]

res = solution(V, edges)
print(res)