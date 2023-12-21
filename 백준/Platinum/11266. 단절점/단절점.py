import sys
sys.setrecursionlimit(10**4+100)
input = sys.stdin.readline

def dfs(node, is_root):
	# 0번 인덱스는 카운트로 사용
    visit_order[0] += 1
    visit_order[node] = visit_order[0]
    child_cnt = 0
    # 최소 진입순서
    min_order = visit_order[node]
    for child in graph[node]:
    	# 이전에 방문한 노드라면 최소 진입순서만 업데이트
        if visit_order[child]:
            min_order = min(min_order, visit_order[child])
            continue
        child_cnt += 1
        res = dfs(child, False)
        min_order = min(min_order, res)
        # 루트노드가 아니고 해당 자식의 최소 진입순서가 같거나 뒤인 경우 현재 노드는 단절점
        if not is_root and res >= visit_order[node]:
            artic_point[node] = 1
    # 만약 루트노드이고 진입가능 자식이 둘 이상인 경우
    if is_root and child_cnt >= 2:
        artic_point[node] = 1
    # 도달가능한 최소 진입순서를 반환
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
# 연결 그래프가 아닐 가능성이 있음
for i in range(1, v+1):
    if not visit_order[i]:
        dfs(i, True)
  	# 단절점 저장
    if artic_point[i]:
        count += 1
        answer.append(i)

print(count)
if count > 0:
    print(*answer)