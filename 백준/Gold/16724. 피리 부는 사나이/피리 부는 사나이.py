import sys
input = sys.stdin.readline

def read_int_list():
    return [*map(int, input().split())]

N, M = read_int_list()
grid = [input() for _ in range(N)]
visited = [[0] * M for _ in range(N)]
group_count = 0
connected_count = 0

for x in range(N):
    for y in range(M):
        if visited[x][y] == 0:
            group_count += 1
            a, b = x, y
            while visited[a][b] == 0:
                visited[a][b] = group_count
                if grid[a][b] == 'U':
                    a -= 1
                elif grid[a][b] == 'D':
                    a += 1
                elif grid[a][b] == 'L':
                    b -= 1
                elif grid[a][b] == 'R':
                    b += 1
            if visited[a][b] == group_count:
                connected_count += 1

print(connected_count)
