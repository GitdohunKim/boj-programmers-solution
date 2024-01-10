import sys; input = sys.stdin.readline
import heapq
from math import inf

def solve():
    N, M, K = map(int, input().split())
    S, D = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b, w = map(int, input().split())
        graph[a].append((b, w))
        graph[b].append((a, w))
    P = [int(input()) for _ in range(K)]

    distance = [[inf] * N for _ in range(N + 1)] 
    distance[S][0] = 0
    queue = [[0, 0, S]] 
    while queue:
        w, visited, here = heapq.heappop(queue)
        flag = False
        for i in range(visited + 1):
            if distance[here][i] < w:
                flag = True
                break
        if visited == N - 1 or flag:
            continue
        for there, ww in graph[here]:
            if distance[there][visited + 1] > distance[here][visited] + ww:
                distance[there][visited + 1] = distance[here][visited] + ww
                heapq.heappush(queue, [distance[there][visited + 1], visited + 1, there])
    answer = inf
    for visited in range(N):
        if answer > distance[D][visited]:
            answer = distance[D][visited]
            limit = visited
    print(answer) 

    tax = 0
    for p in P:
        tax += p 
        answer = inf
        for visited in range(limit + 1): 
            if answer > distance[D][visited] + tax * visited:
                answer = distance[D][visited] + tax * visited
                limit = visited
        print(answer)

solve()