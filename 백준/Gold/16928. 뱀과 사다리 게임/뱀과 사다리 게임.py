from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int,input().split())
dice = [1,2,3,4,5,6]
visited = [False] * 101
dist = [0] * 101
ladder, snake = dict(), dict()
for _ in range(N):
	s, e = map(int,input().split())
	ladder[s] = e
for _ in range(M):
	s, e = map(int,input().split())
	snake[s] = e
 
def bfs(i):
	q = deque()
	q.append(i)
	visited[i] = True
	while q:
		x = q.popleft()
		for k in dice:
			next = x + k
			if 1 <= next <= 100:
				if next in ladder:
					next = ladder[next]
				if next in snake:
					next = snake[next]
				if not visited[next]:
					q.append(next)
					visited[next] = True
					dist[next] = dist[x] + 1
			
bfs(1)
print(dist[100])