import sys
mod = 10 ** 9 + 7
ls = [1, 1]
for i in range(2, 4000001):
    ls.append((ls[-1] * i) % (mod))
for _ in range(int(sys.stdin.readline())):
    n, k = map(int, sys.stdin.readline().split())
    print(((ls[n] * pow(ls[n - k], -1, mod)) % (mod) * pow(ls[k], -1, mod)) % (mod))