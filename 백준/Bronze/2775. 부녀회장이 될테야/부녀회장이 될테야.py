t=int(input())
for i in range(t):
    a=int(input())
    b=int(input())
    blist=[[A for A in range(1,b+1)] for B in range(a+1)]
    for j in range(a):
        sum=0
        for k in range(b):
            sum+=blist[j][k]
            blist[j+1][k]=sum
    print(blist[a][b-1])