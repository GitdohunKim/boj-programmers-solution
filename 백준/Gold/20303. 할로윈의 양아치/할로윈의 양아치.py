import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
candylst = [0] + [*map(int, input().split())]
childs = [*range(N+1)]
friends = [0] + [1 for _ in range(N)]

def root(a):
    if a == childs[a]:
        return a
    childs[a] = root(childs[a])
    return childs[a]

def merge(a, b):
    aroot, broot = root(a), root(b)
    if aroot != broot:
        if aroot > broot:
            friends[broot] += friends[aroot]
            candylst[broot] += candylst[aroot]
            childs[aroot] = broot
        else:
            friends[aroot] += friends[broot]
            candylst[aroot] += candylst[broot]
            childs[broot] = aroot
        return False
    return True

for _ in range(M):
    a, b = map(int, input().split())
    merge(a, b)

selections = [[friends[i], candylst[i]] for i in range(1, N+1) if i == childs[i]]
selections.sort()

bag = [0] * (K+1)
for friendcnt, candycnt in selections:
    for i in range(K, friendcnt-1, -1):
        bag[i] = max(bag[i-friendcnt]+candycnt, bag[i])

print(bag[K-1])
