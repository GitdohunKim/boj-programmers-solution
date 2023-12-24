import sys
import heapq

input = sys.stdin.readline
n, k = map(int, input().split())
items = []
bag = []
candi = []
answer = 0
for _ in range(n):
    # 보석 무게 기준 최소 힙 삽입
    heapq.heappush(items, list(map(int, input().split())))
for _ in range(k):
    bag.append(int(input()))
# 가방 오름차순 정렬
bag = sorted(bag)

for cap in bag:
    # 가방 작은거 부터 꺼내면서 그 가방에 들어가는 보석일단 다 꺼냄.
    # 꺼내서 값을 기준으로 최대힙에 넣음
    while items and items[0][0] <= cap:
        heapq.heappush(candi, -heapq.heappop(items)[1])
    # candi에 현재 가방에 들어갈 수 있는 보석 다들어있음.(최대힙)
    # 이 중 하나 빼면 됨.
    if candi:
        answer += abs(heapq.heappop(candi))
print(answer)