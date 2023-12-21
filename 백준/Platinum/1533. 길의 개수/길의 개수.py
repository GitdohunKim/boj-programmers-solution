MOD = 1000003
N, S, E, T = map(int, input().split())
A = [[0] * (5 * N + 1) for _ in range(5 * N + 1)]
ans = [[0] * (5 * N + 1) for _ in range(5 * N + 1)]

def matrix_multiply(a, b):
    res = [[0] * (5 * N + 1) for _ in range(5 * N + 1)]
    for i in range(1, 5 * N + 1):
        for j in range(1, 5 * N + 1):
            for k in range(1, 5 * N + 1):
                res[i][j] += (a[i][k] * b[k][j]) % MOD
                res[i][j] %= MOD
    return res

def matrix_power():
    global T, A, ans
    while T:
        if T % 2:
            ans = matrix_multiply(ans, A)
        T //= 2
        A = matrix_multiply(A, A)

N_values = []
for i in range(1, N + 1):
    s = input()
    for j in range(len(s)):
        if int(s[j]) >= 1:
            A[i * 5][(j + 1) * 5 - (int(s[j]) - 1)] = 1
    for j in range(1, 5):
        A[(i - 1) * 5 + j][(i - 1) * 5 + j + 1] = 1

for i in range(1, 5 * N + 1):
    ans[i][i] = 1

matrix_power()
print(ans[5 * S][5 * E] % MOD)
