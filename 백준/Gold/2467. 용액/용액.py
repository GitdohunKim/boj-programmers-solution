import sys

input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))

arr.sort()

left, right = 0, N - 1

ans = ()
while left < right:
    if not ans or abs(ans[0] + ans[1]) > abs(arr[left] + arr[right]):
        ans = (arr[left], arr[right])
    if arr[left] + arr[right] > 0:
        right -= 1
    else:
        left += 1
print(ans[0], ans[1])