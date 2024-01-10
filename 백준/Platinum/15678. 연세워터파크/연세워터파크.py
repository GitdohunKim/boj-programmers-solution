from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())

data = [0]+list(map(int, stdin.readline().split()))

stack = deque()

for i in range(1, n+1):
    while stack:
        if stack[0][0]<i-m:
            stack.popleft()
        else:
            data[i] = max(data[i], stack[0][1]+data[i])
            break
    while stack:
        if stack[-1][1]<data[i]:
            stack.pop()
        else:
            break
    stack.append((i, data[i]))

print(max(data[1:]))
        