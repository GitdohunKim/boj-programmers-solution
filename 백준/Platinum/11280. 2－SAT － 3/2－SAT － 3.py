import sys; input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(here):
    visited[here] = True
    for there in graph[here]:
        if not visited[there]:
            dfs(there)
    queue.append(here)

def reverse_dfs(here):
    visited[here] = True
    ids[here] = idx
    for there in reverse_graph[here]:
        if not visited[there]:
            reverse_dfs(there)

N, M = map(int, input().split())
graph = [[] for _ in range(N * 2 + 1)] # 그래프
reverse_graph = [[] for _ in range(N * 2 + 1)] # 역방향

# i v j : ¬i -> j, ¬j -> i
# 둘 중 하나가 거짓이면 하나는 무조건 참이어야 하기 때문.
for _ in range(M):
    i, j = map(int, input().split())
    graph[-i].append(j)
    reverse_graph[j].append(-i)
    graph[-j].append(i)
    reverse_graph[i].append(-j)

# 코사리주
# 정방향 탐색으로 정점 쌓기
queue = []
visited = [False] * (N * 2 + 1)
for here in range(1, N * 2 + 1):
    if not visited[here]:
        dfs(here)
# 역방향 탐색으로 SCC 찾기
visited = [False] * (N * 2 + 1)
ids = [-1] * (N * 2 + 1)
idx = 0
while queue:
    here = queue.pop()
    if not visited[here]:
        reverse_dfs(here)
        idx += 1

# 모든 변수는 역과 같은 SCC이면 안된다. 즉, 모순인지 찾아야 한다.
for i in range(1, N + 1):
    if ids[i] == ids[-i]:
        print(0)
        break
else:
    print(1)