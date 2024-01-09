s=input()
l=len(s)
lst=list(list(0 for _ in range(l)) for _ in range(l))
for y in range(l):
    lst[y][y]=1
    for x in range(y-1,-1,-1):
        lst[y][x]=lst[y][x+1]+lst[y-1][x]+(1 if s[x]==s[y] else -lst[y-1][x+1])
print(lst[l-1][0]%10007)