import sys
input = sys.stdin.readline

from collections import defaultdict

N, M, B = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]

heights = defaultdict(int)
s = min(map(min, ground))
e = max(map(max, ground))

for i in ground:
    for j in i:
        heights[j] += 1

ans_time = sys.maxsize
ans_height = -1

for i in range(s, e+1):
    block_needed = 0
    time = 0

    for k, v in heights.items():
        block_needed += (i-k) * v
    if block_needed > B:
        continue

    for k, v in heights.items():
        diff = i-k

        if diff > 0:
            time += diff * v
            
        elif diff < 0:
            time += (-diff) * v * 2
    
    if time <= ans_time:
        ans_time = time
        ans_height = max(ans_height, i)

print(ans_time, ans_height)