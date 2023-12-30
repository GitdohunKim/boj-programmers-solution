N=int(input())
P=list(map(int,input().split()))
P.sort()
result=[0]*(N+1)
for i in range(1,N+1):
    result[i]=result[i-1]+P[i-1]
print(sum(result))