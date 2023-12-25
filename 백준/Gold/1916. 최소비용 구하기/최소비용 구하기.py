import heapq
import sys
input = sys.stdin.readline 

n = int(input())
m = int(input())

INF = int(1e9)

def dijkstra(start):

    distance[start] = 0

    q = []
    heapq.heappush(q, [0, start])

    while q:
        dist, now = heapq.heappop(q)

        if (distance[now] < dist):
            continue

        for cityInfo in graph[now]: #연결된 도시 번호들
            
            city, cost = cityInfo[0], cityInfo[1]

            cost  = dist + cost
            if distance[city] > cost:
                distance[city] = cost
                heapq.heappush(q,[cost, city])


graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, cost = map(int,input().split())
    graph[start].append([end, cost])

start, end = map(int,input().split())

distance = [INF]* (n+1)
dijkstra(start)

print(distance[end])