l = int(input())
s = input()
ans = 0
mod = 1234567891
for i, x in enumerate(s):
    ans += pow(31, i, mod) * (ord(x) - 96)
    ans %= mod
print(ans)