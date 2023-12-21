import sys
from collections import deque
sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def DFS(curr : int, parent : int) -> int:
    global nodecnt, discover
	
    # 노드 번호를 부여
    nodecnt += 1
    discover[curr] = nodecnt
	
    # 현재 노드의 값
    ret = discover[curr]
	
    # 인접 노드 탐색
    for next in adjlist[curr]:
    	# 부모라면 패스
        if next == parent:
            continue
		
        # 자식 중 번호를 붙이지 않은 노드가 있다면
        if discover[next] == 0:
        	# 자식 중 최소 번호를 찾아냄
            mindisc = DFS(next, curr)
			
        	# 만약 DFS를 통해 찾아낸 최소 번호가 이 노드보다 크다면
            if mindisc > discover[curr]:
            	# 답에 저장
                res.append([min(curr, next), max(curr, next)])
                
            # 최소 번호 저장
            ret = min(ret, mindisc)

        else:
            ret = min(ret, discover[next])

    return ret


V, E = map(int, input().split())

adjlist = [[] for _ in range(V + 1)] # 인접 리스트
discover = [0 for _ in range(V + 1)] # 노드 번호
res = [] # 정답 리스트
nodecnt = 0 # 노드에 번호를 붙이기 위한 정적 변수

# 인접 리스트 
for _ in range(E):
    A, B = map(int, input().split())
    adjlist[A].append(B)
    adjlist[B].append(A)

# 아직 탐색하지 않은 노드를 루트로 DFS 탐색
for v in range(1, V + 1):
    if discover[v] == 0:
        DFS(v, 1)

# 단절선 개수와 오름차순으로 출력
res.sort()
print(len(res))

for x, y in res:
    print(x, y)