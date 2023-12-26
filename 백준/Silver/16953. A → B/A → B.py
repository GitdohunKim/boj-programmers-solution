from collections import defaultdict
from collections import deque

def bfs(start, visited):
    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        x = q.popleft()
        if x == B:
            return visited[x]

        for i in (x * 2, int(str(x) + '1')):
            if 0 <= i <= int(1e9) and not visited[i]:
                q.append(i)
                visited[i] = visited[x] + 1
    return -1


A, B = map(int, input().split())
visited = defaultdict(int)

print(bfs(A, visited))