N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
INF = float('inf')
dp = [[-1] * (1 << N) for _ in range(N)]

def tsp(current, visited):
    if visited == (1 << N) - 1:
        return graph[current][0] if graph[current][0] > 0 else INF
    if dp[current][visited] > 0:
        return dp[current][visited]
    dp[current][visited] = INF
    for next_node in range(N):
        if graph[current][next_node] == 0 or visited & (1 << next_node) != 0:
            continue
        dp[current][visited] = min(dp[current][visited], tsp(next_node, visited | (1 << next_node)) + graph[current][next_node])
    return dp[current][visited]

print(tsp(0, 1))
