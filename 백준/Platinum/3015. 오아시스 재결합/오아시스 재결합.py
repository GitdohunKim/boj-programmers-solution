import sys

n = int(sys.stdin.readline())
oasis = [int(sys.stdin.readline()) for _ in range(n)]

stack = []  # (키, cnt)로 append
result = 0

for o in oasis:
    # 현재 키보다 큰 값이 나올 때까지 스택에서 pop
    while stack and stack[-1][0] < o:
        _, cnt = stack.pop()
        result += cnt

    # 스택이 비어있지 않으면 현재 키와 스택의 끝 값이 같은지 확인
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

# 결과값 출력
print(result)
