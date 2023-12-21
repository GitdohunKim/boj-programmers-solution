import math
import sys
# x^y%m
def powmod(x, y, m):
    r = 1
    while y > 0:
        if y % 2:
            r = (r * x) % m
        y //= 2
        x = x**2 % m
    return r

def miller_rabin(n, a):
    d = (n - 1) // 2
    while (d % 2 == 0):
        if (powmod(a, d, n) == n-1):
            return True
        d //= 2
    tmp = powmod(a, d, n)
    return True if tmp == n-1 or tmp == 1 else False


def isPrime(n):
    if n <= 1:
        return False
    if n <= 100:
        if check[n]:
            return True
        else:
            return False
    for a in alist:
        if not miller_rabin(n, a):
            return False
    return True

check = [True] * 101
for i in range(2, int(math.sqrt(102))+1):
    if check[i]:
        for j in range(i*2, 101, i):
            check[j] = False

t = int(input())
alist = [2, 7, 61]
cnt = 0
for _ in range(t):
    a = int(sys.stdin.readline()) * 2 + 1
    if a % 2 == 1:
        if isPrime(a):
            cnt += 1
print(cnt)