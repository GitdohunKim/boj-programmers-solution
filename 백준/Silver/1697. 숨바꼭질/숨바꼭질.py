from collections import deque

def bfs(start):
    queue = deque([start])
    graph[start] = 1
    
    while queue:
        x = queue.popleft()
        
        for i in (x-1, x+1, x*2):
            if 0 <= i <= 100000 and not graph[i]:
                graph[i] = graph[x] + 1
                queue.append(i)
                
            if i == k:
                return graph[i]-1
            
n, k = map(int, input().split())
graph = [0] * 100001

print(bfs(n))