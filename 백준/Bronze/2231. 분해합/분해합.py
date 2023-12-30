n=int(input())
start=0
if n>=100:
    start=n-100
for i in range(start,n+1):
    tmp=i
    sum=0
    while tmp>=10:
        sum=sum+tmp%10
        tmp=tmp//10
    sum=sum+tmp
    if sum+i==n:
        print(i)
        exit(0)
print(0)
