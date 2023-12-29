n, k = map(int, input().split())

res = 1

for i in range(1, n + 1):
    res *= i

for j in range(1, k + 1):
    res /= j

for k in range(1, n - k + 1):
    res /= k

print(int(res))