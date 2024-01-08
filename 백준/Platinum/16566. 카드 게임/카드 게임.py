import sys
input = sys.stdin.readline

def find_set(x):
    if parent[x] == x:
        return x
    parent[x] = find_set(parent[x])
    return parent[x]

def union(x, y):
    if y == M:
        return

    x, y = find_set(x), find_set(y)
    if x == y:
        return
    if x > y:
        parent[y] = x
    else:
        parent[x] = y

def binarySearch(arr, target):
    start = 0
    end = len(arr) - 1
    while start < end:
        mid = (start + end) // 2
        if arr[mid] > target:
            end = mid
        else:
            start = mid + 1
    return end


N, M, K = map(int, input().split())
card_num = list(map(int, input().split()))
card_num.sort()
player_1 = list(map(int, input().split()))
parent = list(range(N+1))

for i in player_1:
    select = binarySearch(card_num, i)
    select = find_set(select)
    print(card_num[select])
    union(select, select + 1)
