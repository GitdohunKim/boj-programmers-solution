from collections import deque
import sys

input = sys.stdin.readline

def bfs(r, c):
    q = deque()
    q.append((r, c))
    visited[r][c] = 1
    cnt = 1
    while q:
        prev_r, prev_c = q.popleft()
        zero[prev_r][prev_c] = group_num
        for dx, dy in directions:
            next_r = prev_r + dx
            next_c = prev_c + dy
            if 0 <= next_r < N and 0 <= next_c < M:
                if not visited[next_r][next_c] and not board[next_r][next_c]:
                    q.append((next_r, next_c))
                    visited[next_r][next_c] = 1
                    cnt += 1
    return cnt

def get_ans(r, c):
    pos = set()
    for dx, dy in directions:
        next_r = r + dx
        next_c = c + dy
        if 0 <= next_r < N and 0 <= next_c < M:
            if zero[next_r][next_c]:
                pos.add(zero[next_r][next_c])
    ans = (1 + sum(zero_dict[p] for p in pos)) % 10
    return ans

N, M = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
zero = [[0] * M for _ in range(N)]
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
group_num = 1
zero_dict = dict()

for i in range(N):
    for j in range(M):
        if not board[i][j] and not visited[i][j]:
            cnt = bfs(i, j)
            zero_dict[group_num] = cnt
            group_num += 1

ans = [[get_ans(i, j) if board[i][j] else 0 for j in range(M)] for i in range(N)]

for row in ans:
    print("".join(map(str, row)))
