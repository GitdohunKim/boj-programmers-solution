n, m = map(int, input().split())
trees = list(map(int, input().split()))
low, high = 0, max(trees)
maxLen = 0

while low <= high:
    mid = (low + high) // 2

    cutLen = 0
    for tLen in trees:
        if mid < tLen:
            cutLen += tLen - mid
            
    if m <= cutLen:
        low = mid + 1
        maxLen = max(mid, maxLen)
    else:
        high = mid - 1

print(maxLen)
