import sys
import bisect

def LIS():
    arr = [A[0]]
    num = [1] * n

    for i in range(1, n):
        if arr[-1] < A[i]:
            arr.append(A[i])
            num[i] = len(arr)
        else:
            idx = bisect.bisect_left(arr, A[i])
            arr[idx] = A[i]
            num[i] = idx + 1

    print(n - len(arr))
    m = len(arr)
    k = []

    for i in range(n-1, -1, -1):
        if m == 0:
            break
        if num[i] == m:
            m -= 1
            k.append(A[i])

    for i in range(n):
        if A[i] not in k:
            print(T[i])

n = int(sys.stdin.readline())
L = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
L.sort()

A = [L[i][1] for i in range(n)]
T = [L[i][0] for i in range(n)]

LIS()
