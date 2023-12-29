import sys
input = sys.stdin.readline
n,k = map(int,input().split())
arr=[]
for i in range(n):
    arr.append(int(input()))

st = 1
ed = sum(arr)//k
ans=0
while st<=ed:
    mid=(st+ed)//2
    cal = sum([x//mid for x in arr])
    if cal >= k:
        st = mid+1
        ans = mid
    else:
        ed = mid-1

print(ans)