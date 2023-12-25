import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    queue = deque()
    queue.append((0, 0, board[0][0]))
    visited = set()
    visited.add((0, 0, board[0][0]))
    max_cnt = 0

    while queue:
        y, x, v = queue.pop()
        max_cnt = max(max_cnt, len(v))

        for dy, dx in direction:
            ny, nx = y + dy, x + dx

            if 0 <= ny < R and 0 <= nx < C and board[ny][nx] not in v and (ny, nx, v + board[ny][nx]) not in visited:
                visited.add((ny, nx, v + board[ny][nx]))
                queue.append((ny, nx, v + board[ny][nx]))

    return max_cnt


R, C = map(int, input().split())
board = [input() for _ in range(R)]

direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]

print(bfs())