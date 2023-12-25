from sys import stdin

def solution(V, edges):

    answer = 0

    # Union & Find
    parent = [i for i in range(V+1)]
    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]
    def union(x,y):
        x = find(x)
        y = find(y)
        parent[max(x,y)] = parent[min(x,y)]

    # 가중치(x[2])를 기준으로 오름차순으로 정렬
    edges.sort(key = lambda x : x[2])

    for s, e, w in edges:
        # 싸이클이 생기지 않으면
        if find(s) != find(e):
            # 해당 간선 연결
            union(s,e)
            # 해당 간선의 가중치 누적합
            answer += w

    return answer

# input
V, E = map(int,stdin.readline().split())
edges = [list(map(int,stdin.readline().split())) for _ in range(E)]

# response
res = solution(V, edges)
print(res)