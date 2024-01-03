import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(node, weight):
    for w, n in tree[node]:
        if dist[n] == -1:
            dist[n] = weight + w
            dfs(n, weight + w)

n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    tree[a].append([c, b])
    tree[b].append([c, a])

dist = [-1] * (n + 1)  
dist[1] = 0
dfs(1, 0)  

start = dist.index(max(dist))  
dist = [-1] * (n + 1)
dist[start] = 0 
dfs(start, 0)

print(max(dist))