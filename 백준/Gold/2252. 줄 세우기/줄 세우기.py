from collections import deque

def topological_sort(N, M, edges):
    A = [[] for _ in range(N + 1)]
    D = [0] * (N + 1)

    for start, end in edges:
        A[start].append(end)
        D[end] += 1

    queue = deque()

    for i in range(1, N + 1):
        if D[i] == 0:
            queue.append(i)

    result = []
    while queue:
        now = queue.popleft()
        result.append(now)
        for next_node in A[now]:
            D[next_node] -= 1
            if D[next_node] == 0:
                queue.append(next_node)

    return result

if __name__ == "__main__":
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]

    result = topological_sort(N, M, edges)

    print(*result)
