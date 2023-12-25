import sys
input = sys.stdin.readline
from collections import deque
def bfs(start,n,m):
    visited = set()
    
    queue = deque([(start,None)])
    while queue:
        curr,parents = queue.popleft()
        if curr in visited:
                return True
        visited.add(curr)

        for neighbor in find(curr,n,m):
            if neighbor != parents:
                queue.append((neighbor,curr))
    return False

def find(node,n,m):
    x,y = divmod(node,m)
    mark = arr[x][y]
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    neighbor = []
    for dx,dy in directions:
        nx,ny = x + dx , y + dy
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == mark:
            neighbor.append(nx * m + ny)
    
    return neighbor

def made(n,m):
    for node in range(n*m):
            if bfs(node,n,m):
                return 'Yes'
    return 'No'

while 1:
    n,m = map(int,input().split())
    arr = [list(input().strip()) for _ in range(n)]
    print(made(n,m))
    break