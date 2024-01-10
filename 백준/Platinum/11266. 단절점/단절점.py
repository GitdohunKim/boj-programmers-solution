import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

def dfs(node, is_root):
    visit_order[0] += 1
    visit_order[node] = visit_order[0]
    child_cnt = 0
    min_order = visit_order[node]
    
    for child in graph[node]:
        if visit_order[child]:
            min_order = min(min_order, visit_order[child])
            continue
        child_cnt += 1
        res = dfs(child, False)
        min_order = min(min_order, res)
        
        if not is_root and res >= visit_order[node]:
            artic_point[node] = 1
            
    if is_root and child_cnt >= 2:
        artic_point[node] = 1
        
    return min_order
    
v, e = map(int, input().rstrip().split())

graph = [[] for _ in range(v+1)]
visit_order = [0]*(v+1)
artic_point = [0]*(v+1)

for _ in range(e):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0
answer = []

for i in range(1, v+1):
    if not visit_order[i]:
        dfs(i, True)
        
    if artic_point[i]:
        count += 1
        answer.append(i)

print(count)
if count > 0:
    print(*answer)
