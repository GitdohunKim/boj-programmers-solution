import sys

input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())

DP = [[INF] * N for _ in range(N)]
graph = []

for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    DP[a][b] = DP[b][a] = min(DP[a][b], c)
    graph.append((a, b, c))

for k in range(N):
    for i in range(N):
        for j in range(N):
            DP[i][j] = min(DP[i][j], DP[i][k] + DP[k][j])

for i in range(N):
    DP[i][i] = 0

result = INF

for i in range(N):
    MAX = 0
    for a, b, c in graph:
        MAX = max(MAX, (DP[i][a] + c + DP[b][i]) / 2)
    result = min(result, MAX)

print(result)
