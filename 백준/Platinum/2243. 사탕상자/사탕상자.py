import sys

def input():
    return sys.stdin.readline().rstrip()

def change(target, diff, idx, start, end):
    if end < target or target < start:
        return 

    tree[idx] += diff
    if start != end:
        change(target, diff, idx * 2, start, (start + end) // 2)
        change(target, diff, idx * 2 + 1, (start + end) // 2 + 1, end)

def print_sum(count, idx, start, end):
    if start == end: 
        return start
    else:
        if tree[idx * 2] >= count:
            return print_sum(count, idx * 2, start, (start + end) // 2)
        else:
            return print_sum(count - tree[idx * 2], idx * 2 + 1, (start + end) // 2 + 1, end)

N = 1000000 
nums = [0] * (N + 1)
tree = [0] * (2 ** 21)

M = int(input())
for _ in range(M):
    order, *content = map(int, input().split())
    if order > 1:
        change(content[0], content[1], 1, 1, N)
        nums[content[0]] += content[1]
    else:
        eat = print_sum(content[0], 1, 1, N)
        print(eat)
        change(eat, -1, 1, 1, N)
        nums[eat] += -1
