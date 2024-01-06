def prime_list(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i]:
            for j in range(i + i, n, i):
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i]]
N = int(input())
num = prime_list(N + 1)
ans = 0
start, end = 0, 0
while end <= len(num):
    tmp = sum(num[start : end])
    if tmp == N:
        ans += 1
        end += 1
    elif tmp < N:
        end += 1
    else:
        start += 1
print(ans)