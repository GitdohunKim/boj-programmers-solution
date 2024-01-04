import heapq

def dijkstra(graph, start, dist, items, max_weight):
    n = len(graph)
    dijkstra_result = [float('inf')] * n
    dijkstra_result[start] = 0
    heap = [(0, start)]

    while heap:
        current_weight, current_node = heapq.heappop(heap)

        if current_weight > dijkstra_result[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            new_distance = dijkstra_result[current_node] + weight

            if new_distance < dijkstra_result[neighbor]:
                dijkstra_result[neighbor] = new_distance
                heapq.heappush(heap, (new_distance, neighbor))

    total_items = 0
    for i, distance in enumerate(dijkstra_result):
        if distance <= max_weight:
            total_items += items[i-1]

    return total_items

def main():
    N, M, R = map(int, input().split())
    items = list(map(int, input().split()))

    # 그래프 생성
    adj = [[] for _ in range(N+1)]
    dist = [[0 for _ in range(N+1)] for _ in range(N+1)]
    
    for _ in range(R):
        a, b, c = map(int, input().split())
        adj[a].append((b, c))
        adj[b].append((a, c))
        dist[a][b] = c
        dist[b][a] = c

    max_collected_items = 0
    for start_node in range(1, N+1):
        collected_items = dijkstra(adj, start_node, dist, items, M)
        max_collected_items = max(max_collected_items, collected_items)

    print(max_collected_items)

if __name__ == "__main__":
    main()
