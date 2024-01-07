import sys

def dfs(x, y, cnt, L, R):
    global ans
    if x == n:
        ans = max(cnt, ans)
        return

    if y >= n:
        if n % 2 == 0:
            if y == n:
                dfs(x+1, 1, cnt, L, R)
            else:
                dfs(x+1, 0, cnt, L, R)
        else:
            if y == n:
                dfs(x+1, 0, cnt, L, R)
            else:
                dfs(x+1, 1, cnt, L, R)
        return

    if board[x][y] == 1 and not L[x+y] and not R[x-y+n-1]:
        L[x+y] = 1
        R[x-y+n-1] = 1
        dfs(x, y+2, cnt+1, L, R)
        L[x+y] = 0
        R[x-y+n-1] = 0
    dfs(x, y+2, cnt, L, R)

if __name__ == "__main__":
    n = int(input().strip())
    board = [list(map(int, input().strip().split())) for _ in range(n)]

    def solve():
        global ans
        L = [0] * (n * 2 - 1)
        R = [0] * (n * 2 - 1)
        ans = 0
        dfs(0, 0, 0, L, R)
        b = ans
        ans = 0
        dfs(0, 1, 0, L, R)
        w = ans
        print(w + b)

    solve()
