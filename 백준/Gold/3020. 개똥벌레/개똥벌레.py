import sys
input = sys.stdin.readline

N, H = map(int, input().split())

obstacle = [0] * H


for i in range(N):
    if (i%2 ==0):
        d = int(input())
        obstacle[H-d] +=1 
    else:
        u = int(input())
        obstacle[0] += 1 
        obstacle[u] -= 1 

for i in range(1, H):
    obstacle[i] += obstacle[i-1]


minn = min(obstacle)
cnt = obstacle.count(minn)

print(minn, cnt)