import sys
import math

input = sys.stdin.readline

def build(idx, L, R):
    if L == R:
        seg[idx] = L
        return L
    
    mid = (L + R) // 2
    Li, Ri = build(2 * idx, L, mid), build(2 * idx + 1, mid + 1, R)
    
    seg[idx] = Li if arr[Li] <= arr[Ri] else Ri
    return seg[idx]

def update(idx, L, R, tar):
    if tar < L or R < tar:
        return seg[idx]
    if L == R:
        seg[idx] = tar
        return seg[idx]
    
    mid = (L + R) // 2
    Li, Ri = update(2 * idx, L, mid, tar), update(2 * idx + 1, mid + 1, R, tar)
    
    seg[idx] = Li if arr[Li] <= arr[Ri] else Ri
    return seg[idx]

def query(idx, L, R, S, E):
    if R < S or E < L:
        return 0
    if S <= L and R <= E:
        return seg[idx]
    
    mid = (L + R) // 2
    Li, Ri = query(2 * idx, L, mid, S, E), query(2 * idx + 1, mid + 1, R, S, E)

    return Li if arr[Li] <= arr[Ri] else Ri

N = int(input())
arr = [10 ** 9 + 1] + [*map(int, input().split())]
seg = [0] * (1 << math.ceil(math.log2(N)) + 1)

build(1, 1, N)
for _ in range(int(input())):
    n, i, j = map(int, input().split())
    
    if n == 1:
        arr[i] = j
        update(1, 1, N, i)
    else:
        print(query(1, 1, N, i, j))
