a = int(input())
b = list(map(int,input().split()))
b.sort()
d = 0
for i in range(a):
    c = 0
    if b[i] == 1:
        continue
    for j in range(1,b[i]+1):
        if b[i]%j == 0:
            c += 1
    if c == 2:
        d += 1
print(d)