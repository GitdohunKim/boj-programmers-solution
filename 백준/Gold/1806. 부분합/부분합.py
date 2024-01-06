import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

st, en = 0, 0
minimum = sys.maxsize
tmp = nums[0]

while st <= en and en < N:
    if tmp < M:
        en += 1
        if en < N:
            tmp += nums[en]
    else:
        minimum = min(en - st, minimum)
        tmp -= nums[st]
        st += 1

print(minimum + 1 if minimum != sys.maxsize else 0)
