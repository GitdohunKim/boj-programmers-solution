import sys
input = sys.stdin.readline

def init_tree(start, end, index, tree, func):
    if start == end:
        tree[index] = integers[start]
        return tree[index]
    mid = (start + end) // 2
    tree[index] = func(init_tree(start, mid, index * 2, tree, func), init_tree(mid + 1, end, index * 2 + 1, tree, func))
    return tree[index]

def query(start, end, index, left, right, tree, func, default):
    if right < start or left > end:
        return default
    if left <= start and end <= right:
        return tree[index]
    mid = (start + end) // 2
    return func(query(start, mid, index * 2, left, right, tree, func, default),
                query(mid + 1, end, index * 2 + 1, left, right, tree, func, default))

N, M = map(int, input().split())
integers = [int(input()) for _ in range(N)]

max_tree = [0] * (4 * N)
min_tree = [float('inf')] * (4 * N)

init_tree(0, N - 1, 1, max_tree, max)
init_tree(0, N - 1, 1, min_tree, min)

for _ in range(M):
    a, b = map(int, input().split())
    ans_min = query(0, N - 1, 1, a - 1, b - 1, min_tree, min, float('inf'))
    ans_max = query(0, N - 1, 1, a - 1, b - 1, max_tree, max, 0)
    print(ans_min, ans_max)
