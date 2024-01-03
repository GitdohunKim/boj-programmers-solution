import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
parents = [0 for _ in range(n+1)]
parents[1] = 1

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(start):
    for node in tree[start]:
        if parents[node] == 0:
            parents[node] = start
            dfs(node)

dfs(1)

print(*parents[2:])
