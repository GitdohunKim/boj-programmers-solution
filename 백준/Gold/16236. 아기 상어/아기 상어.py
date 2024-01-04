import sys
import heapq

input = sys.stdin.readline

N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]

def solution():
    size = 2
    cnt = 0
    result = 0

    q = []
    for i in range(N):
        for j in range(N):
            if space[i][j] == 9:
                space[i][j] = 0
                heapq.heappush(q, (0, i, j))
                break

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[False] * N for _ in range(N)]

    while q:
        d, x, y = heapq.heappop(q)

        if 0 < space[x][y] < size:
            space[x][y] = 0
            cnt += 1
            if cnt == size:
                size += 1
                cnt = 0
            result += d
            d = 0
            q.clear()
            visited = [[False] * N for _ in range(N)]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and space[nx][ny] <= size:
                visited[nx][ny] = True
                heapq.heappush(q, (d + 1, nx, ny))

    return result

print(solution())
