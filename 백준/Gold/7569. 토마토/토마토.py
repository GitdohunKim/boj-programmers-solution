from collections import deque

m, n, h = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]

rippen = []

for i in range(h):
  for j in range(n):
    for k in range(m):
      if arr[i][j][k] == 1:
        rippen.append((i, j, k, 0))

q = deque(rippen)
max_depth = 0
while q:
  a, b, c, depth = q.popleft()
  if depth > max_depth:
    max_depth = depth
  
  for x, y, z in [(a-1, b, c), (a, b-1, c), (a, b, c-1), (a+1, b, c), (a, b+1, c), (a, b, c+1)]:
    if 0<=x<h and 0<=y<n and 0<=z<m and arr[x][y][z] == 0 and visited[x][y][z] == False:
      visited[x][y][z] = True
      arr[x][y][z] = 1
      q.append((x, y, z, depth+1))

for i in range(h):
  for j in range(n):
    for k in range(m):
      if arr[i][j][k] == 0:
        print(-1)
        exit()

print(depth)