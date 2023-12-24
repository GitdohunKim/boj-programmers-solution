INF = 50000000

def bf(i:int):
    # i --> 시작 지점
    dis = [INF] * (N+1)
    dis[i] = 0 # 시작위치의 거리 가중치 초기화
    
    # 뺑뺑이 있는지 찾기 위해서 N번 반복
    for cnt in range(N):
        for edge in edges:
            cur = edge[0]
            goal = edge[1]
            weight = edge[2]
            if dis[goal] > dis[cur] + weight:
                dis[goal] = dis[cur] + weight

                # 음의 사이클 존재
                if cnt == N-1:
                    return True
    #음수 사이클 없음
    return False




TC = int(input())

for tc in range(TC):
    N,M,W = map(int,input().split())
    # 그래프 인접 리스트
    edges = []
    # 도로 그래프 입력
    for _ in range(M):
        S,E,T = map(int,input().split())
        edges.append([S,E,T])
        edges.append([E,S,T])
    #웜홀 정보 입력
    for _ in range(W):
        S,E,T = map(int,input().split())
        edges.append([S,E,-T])

    negative_cycle_exist = bf(1)
    # 음수 사이클이 존재하는지를 확인하는 것
    print('YES' if negative_cycle_exist else 'NO') 