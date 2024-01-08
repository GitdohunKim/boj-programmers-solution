from sys import stdin

def main():
    Sr = stdin.readline
    N = int(Sr()) - 1
    mod = 10**9 + 7

    A = list(map(int, Sr().split()))
    A.sort()

    D = [1]
    a = 1
    for i in range(N + 1):
        a *= 2
        a %= mod
        D.append(a)

    B = 0
    h = D[N] + 1
    for i in range(N):
        k = A[i + 1] - A[i]
        B += (k * (h - D[i + 1])) % mod
        h += D[N - i - 1]

    print(B % mod)

if __name__ == "__main__":
    main()
