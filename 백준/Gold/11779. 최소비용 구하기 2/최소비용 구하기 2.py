from sys import stdin
from collections import defaultdict
from heapq import heappush, heappop

input = stdin.readline

def build_graph(m):
    graph = defaultdict(lambda: defaultdict(int))
    for _ in range(m):
        a, b, c = map(int, input().split())
        if b in graph[a].keys():
            if graph[a][b] > c:
                graph[a][b] = c
        else:
            graph[a][b] = c
    return graph

def dijkstra(graph, start, end, n):
    INF = n * 100000
    distance = [INF] * (n + 1)
    trace = [-1] * (n + 1)
    queue = []

    distance[start] = 0
    heappush(queue, (0, start))

    while queue:
        dist, cur = heappop(queue)

        if dist > distance[cur]:
            continue

        for v, cost in graph[cur].items():
            cost = dist + cost
            if cost < distance[v]:
                distance[v] = cost
                trace[v] = cur
                heappush(queue, (cost, v))

    return distance, trace

def print_result(distance, trace, end):
    print(distance[end])

    s = end
    history = []
    while s != -1:
        history.append(s)
        s = trace[s]
    print(len(history))
    print(*history[::-1])

def solution():
    n = int(input())
    m = int(input())

    graph = build_graph(m)

    start, end = map(int, input().split())  # 수정

    distance, trace = dijkstra(graph, start, end, n)

    print_result(distance, trace, end)

solution()
