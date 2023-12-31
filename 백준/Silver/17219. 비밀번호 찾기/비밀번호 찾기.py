import sys
input = sys.stdin.readline
n, m = map(int, input().split())
d = {}
for i in range(n):
    a, b = map(str, input().rstrip().split())
    d[a] = b
for j in range(m):
    print(d[input().rstrip()])