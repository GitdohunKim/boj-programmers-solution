import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
oasis = [int(input()) for _ in range(n)]

stack = []  
result = 0

for o in oasis:
    while stack and stack[-1][0] < o:
        _, cnt = stack.pop()
        result += cnt

    if stack:
        if stack[-1][0] == o:
            cnt = stack.pop()[1]
            result += cnt

            if stack:
                result += 1
            stack.append((o, cnt + 1))
        else:
            stack.append((o, 1))
            result += 1
    else:
        stack.append((o, 1))

print(result)
