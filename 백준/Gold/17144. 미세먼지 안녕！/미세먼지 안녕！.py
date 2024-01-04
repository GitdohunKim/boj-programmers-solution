import sys
from math import trunc

def spread(R, C):
    change = [[0 for _ in range(C)] for _ in range(R)]

    for r in range(R):
        for c in range(C):
            amount = trunc(arr[r][c] / 5) 
            if amount == 0:
                continue

            for i, j in t_move:
                nr, nc = r + i, c + j
                if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] != -1:
                    change[nr][nc] += amount
                    change[r][c] -= amount

    for r in range(R):
        for c in range(C):
            arr[r][c] += change[r][c]

def clean(t, s, e, C, move):
    start = (t, 0)
    r, c = t, 0
    last = 0

    for i, j in move:
        while True:
            nr, nc = r + i, c + j

            if (nr, nc) == start:
                break

            if s <= nr < e and 0 <= nc < C:
                now = arr[nr][nc]
                arr[nr][nc] = last
                last = now
            else:
                break

            r, c = nr, nc

input = sys.stdin.readline
t_move = [[0, 1], [-1, 0], [0, -1], [1, 0]]
b_move = [[0, 1], [1, 0], [0, -1], [-1, 0]]

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
top = 0

for i in range(R):
    if arr[i][0] == -1:
        top = i
        break

for _ in range(T):
    spread(R, C)

    clean(top, 0, top + 1, C, t_move)
    clean(top + 1, top + 1, R, C, b_move)

result = 2
for i in range(R):
    for j in range(C):
        result += arr[i][j]

print(result)
