import sys
input=sys.stdin.readline
arr = [list(map(int, input().split())) for _ in range(int(input()))]
arr.sort(key=lambda x : (x[1],x[0]))
for x,y in arr:
    print(x,y)