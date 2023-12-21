import heapq, sys

# dijkstra1 : 현재 정점 v에서 출발하여 각 정점의 최단거리를 갱신하는 함수
def dijstra1(v):
    d[v] = 0
    q = []
    q.append((0, v))
    while q:
        cur_dist, cur = heapq.heappop(q)
        if d[cur] < cur_dist:
            continue
        for (next, next_dist) in adj[cur]:
            # 다익스트라 갱신 조건을 만족하면서 현재 간선이 최단 경로가 아닌 경우
            if next_dist + cur_dist < d[next] and check[cur][next] == False:
                d[next] = next_dist + cur_dist
                heapq.heappush(q, (next_dist + cur_dist, next))

# dijkstra2 : 현재 정점 v에서 출발하여 최단 경로 간선을 지우는 함수
def dijstra2(v):
    q = []
    q.append((d[v], v))
    while q:
        cur_dist, cur = heapq.heappop(q)
        # 현재점이 시작점이면 탐색 종료
        if cur == s:
            continue
        for (past, past_dist) in rev_adj[cur]:
            # 이미 최단 경로라면 탐색 종료
            if check[past][cur] == True:
                continue
            # 최단 경로 상의 간선인 경우
            if d[past] == d[cur] - past_dist:
                check[past][cur] = True
                heapq.heappush(q, (d[past], past))

INF = 9876543210
while True:
    # 입력부
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:
        break
    s, e = map(int, sys.stdin.readline().split())
    
    # adj : 일반적 인접리스트
    # rev_adj : 방향을 바꾼 역인접리스트
    adj = [[] for _ in range(n)]
    rev_adj = [[] for _ in range(n)]
    # check : (i, j)를 잇는 간선이 최단 경로 상에 있는 간선인지 아닌지 나타내는 2차원 배열
    check = [[False] * n for _ in range(n)]
    
    # d : 시작점에서 출발하여 각 점의 최단거리를 저장하는 배열
    d = [INF] * n
    for i in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        adj[a].append((b, c))
        rev_adj[b].append((a, c))
    # 첫 다익스트라1로 d 갱신
    dijstra1(s)
    # 이후 다익스트라2로 check 갱신
    dijstra2(e)
    
    # 거리 배열 초기화 후 두번째 다익스트라로 최단 경로 상의 간선을 배제한 최단 경로 갱신
    for i in range(n):
        d[i] = INF
    dijstra1(s)
    
    # 문제의 조건에 따라 정답 출력
    print(d[e] if d[e] != INF else -1)