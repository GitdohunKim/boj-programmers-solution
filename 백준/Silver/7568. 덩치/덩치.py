import sys
N = int(sys.stdin.readline().strip())
info = []
for _ in range(N):
    w, h = map(int, sys.stdin.readline().strip().split())
    info.append([w,h])
order = [1 for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == j:
            pass
        else:
            if info[i][0] < info[j][0] and info[i][1] < info[j][1]:
                order[i] += 1
    print(order[i], end = ' ')
              
 